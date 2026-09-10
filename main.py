import json
import os
import sqlite3
import io

from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from pydantic import BaseModel

from pypdf import PdfReader
from docx import Document

from career_model import recommend_career as ai_recommend_career


# =========================================================
# CONFIGURATION
# =========================================================

load_dotenv(override=True)

app = FastAPI(title="CareerMate AI")


api_key = os.getenv(
    "OPENROUTER_API_KEY",
    ""
).strip().strip('"').strip("'")


if not api_key:
    print("WARNING: OPENROUTER_API_KEY is not configured.")


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# DATABASE
# =========================================================

def get_connection():

    connection = sqlite3.connect(
        "careermate.db"
    )

    connection.row_factory = sqlite3.Row

    return connection


# =========================================================
# CREATE DATABASE TABLES
# =========================================================

connection = get_connection()
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    university TEXT NOT NULL,
    major TEXT NOT NULL,
    year INTEGER NOT NULL,
    skills TEXT NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    interests TEXT NOT NULL,
    favorite_subjects TEXT NOT NULL,
    work_style TEXT NOT NULL,
    experience_level TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")


connection.commit()
connection.close()


# =========================================================
# PYDANTIC MODELS
# =========================================================

class StudentProfile(BaseModel):

    name: str
    university: str
    major: str
    year: int
    skills: list[str]


class CareerAssessment(BaseModel):

    student_id: int
    interests: list[str]
    favorite_subjects: list[str]
    work_style: str
    experience_level: str


class CareerRecommendationRequest(BaseModel):

    student_id: int


class CareerAssistantRequest(BaseModel):

    student_id: int
    question: str


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():

    return {
        "message": "CareerMate AI is running with OpenRouter!"
    }


# =========================================================
# CREATE STUDENT
# =========================================================

@app.post("/students")
def create_student(
    student: StudentProfile
):

    connection = get_connection()
    cursor = connection.cursor()

    skills_text = ", ".join(
        student.skills
    )

    cursor.execute(
        """
        INSERT INTO students
        (name, university, major, year, skills)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            student.name,
            student.university,
            student.major,
            student.year,
            skills_text,
        ),
    )

    connection.commit()

    student_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Student profile created successfully",

        "student_id": student_id,

        "student": {
            "name": student.name,
            "university": student.university,
            "major": student.major,
            "year": student.year,
            "skills": student.skills,
        },
    }


# =========================================================
# GET ALL STUDENTS
# =========================================================

@app.get("/students")
def get_students():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    connection.close()

    return {
        "students": [
            dict(student)
            for student in students
        ]
    }


# =========================================================
# GET STUDENT
# =========================================================

@app.get("/students/{student_id}")
def get_student(
    student_id: int
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE id = ?
        """,
        (student_id,),
    )

    student = cursor.fetchone()

    connection.close()

    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student": dict(student)
    }


# =========================================================
# CREATE ASSESSMENT
# =========================================================

@app.post("/assessment")
def create_assessment(
    assessment: CareerAssessment
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id
        FROM students
        WHERE id = ?
        """,
        (assessment.student_id,),
    )

    student = cursor.fetchone()

    if student is None:

        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    interests_text = ", ".join(
        assessment.interests
    )

    subjects_text = ", ".join(
        assessment.favorite_subjects
    )

    cursor.execute(
        """
        INSERT INTO assessments
        (
            student_id,
            interests,
            favorite_subjects,
            work_style,
            experience_level
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            assessment.student_id,
            interests_text,
            subjects_text,
            assessment.work_style,
            assessment.experience_level,
        ),
    )

    connection.commit()

    assessment_id = cursor.lastrowid

    connection.close()

    return {

        "message":
            "Career assessment created successfully",

        "assessment_id":
            assessment_id,

        "assessment": {

            "student_id":
                assessment.student_id,

            "interests":
                assessment.interests,

            "favorite_subjects":
                assessment.favorite_subjects,

            "work_style":
                assessment.work_style,

            "experience_level":
                assessment.experience_level,
        },
    }


# =========================================================
# GET ALL ASSESSMENTS
# =========================================================

@app.get("/assessments")
def get_assessments():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM assessments"
    )

    assessments = cursor.fetchall()

    connection.close()

    return {
        "assessments": [
            dict(assessment)
            for assessment in assessments
        ]
    }


# =========================================================
# GET STUDENT ASSESSMENT
# =========================================================

@app.get(
    "/students/{student_id}/assessment"
)
def get_student_assessment(
    student_id: int
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM assessments
        WHERE student_id = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (student_id,),
    )

    assessment = cursor.fetchone()

    connection.close()

    if assessment is None:

        raise HTTPException(
            status_code=404,
            detail="Assessment not found for this student"
        )

    return {
        "assessment":
            dict(assessment)
    }


# =========================================================
# CAREER RECOMMENDATION
# =========================================================

@app.post("/recommend")
def recommend_career(
    request: CareerRecommendationRequest
):

    connection = get_connection()
    cursor = connection.cursor()

    # -----------------------------------------------------
    # Get student
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE id = ?
        """,
        (request.student_id,),
    )

    student = cursor.fetchone()

    if student is None:

        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # -----------------------------------------------------
    # Get latest assessment
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT *
        FROM assessments
        WHERE student_id = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (request.student_id,),
    )

    assessment = cursor.fetchone()

    connection.close()

    if assessment is None:

        raise HTTPException(
            status_code=404,
            detail="Assessment not found for this student"
        )

    # -----------------------------------------------------
    # Convert database data
    # -----------------------------------------------------

    skills = [
        skill.strip()
        for skill in student["skills"].split(",")
        if skill.strip()
    ]

    interests = [
        interest.strip()
        for interest
        in assessment["interests"].split(",")
        if interest.strip()
    ]

    favorite_subjects = [
        subject.strip()
        for subject
        in assessment["favorite_subjects"].split(",")
        if subject.strip()
    ]

    # -----------------------------------------------------
    # Run CareerMate Career Engine
    # -----------------------------------------------------

    result = ai_recommend_career(

        skills=skills,

        interests=interests,

        favorite_subjects=favorite_subjects,

        work_style=
            assessment["work_style"],

        experience_level=
            assessment["experience_level"],
    )

    return {

        "student_id":
            request.student_id,

        "recommended_career":
            result["career"],

        "match_score":
            result["score"],

        "reason":
            result["reason"],

        "current_skills":
            result["current_skills"],

        "skill_gaps":
            result["skill_gaps"],

        "skills_to_learn":
            result["skills_to_learn"],

        "optional_skills":
            result["optional_skills"],

        "roadmap":
            result["roadmap"],

        "top_recommendations":
            result["top_recommendations"],

        "message":
            "Career recommendation generated successfully",
    }


# =========================================================
# CAREER ASSISTANT
# =========================================================

@app.post("/career-assistant")
def career_assistant(
    request: CareerAssistantRequest
):

    # -----------------------------------------------------
    # Get recommendation
    # -----------------------------------------------------

    recommendation = recommend_career(
        CareerRecommendationRequest(
            student_id=request.student_id
        )
    )

    career = recommendation[
        "recommended_career"
    ]

    score = recommendation[
        "match_score"
    ]

    current_skills = recommendation.get(
        "current_skills",
        []
    )

    skill_gaps = recommendation.get(
        "skill_gaps",
        []
    )

    optional_skills = recommendation.get(
        "optional_skills",
        []
    )

    roadmap = recommendation[
        "roadmap"
    ]

    reason = recommendation[
        "reason"
    ]

    # -----------------------------------------------------
    # Get student information
    # -----------------------------------------------------

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            name,
            university,
            major,
            year,
            skills
        FROM students
        WHERE id = ?
        """,
        (request.student_id,),
    )

    student = cursor.fetchone()

    # -----------------------------------------------------
    # Get assessment
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT
            interests,
            favorite_subjects,
            work_style,
            experience_level
        FROM assessments
        WHERE student_id = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (request.student_id,),
    )

    assessment = cursor.fetchone()

    connection.close()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # -----------------------------------------------------
    # Student data
    # -----------------------------------------------------

    name = student["name"]
    university = student["university"]
    major = student["major"]
    year = student["year"]
    student_skills = student["skills"]

    if assessment:

        interests = assessment[
            "interests"
        ]

        favorite_subjects = assessment[
            "favorite_subjects"
        ]

        work_style = assessment[
            "work_style"
        ]

        experience_level = assessment[
            "experience_level"
        ]

    else:

        interests = "Not provided"
        favorite_subjects = "Not provided"
        work_style = "Not provided"
        experience_level = "Not provided"

    # -----------------------------------------------------
    # System Prompt
    # -----------------------------------------------------

    system_prompt = """
You are CareerMate AI.

You are a simple, friendly and practical
career assistant for university students.

Answer the student's question clearly.

IMPORTANT RULES:

1. Always use numbered sections.

2. Each section must have a bold title.

3. Under each title use short bullet points
   starting with "-".

4. Do not write long paragraphs.

5. Keep the answer beginner-friendly.

6. If the student asks in Arabic,
   answer in Egyptian Arabic.

7. Stay focused on the student's
   recommended career.

8. Do not invent skills that are not
   relevant to the recommended career.

9. If the student asks what to learn,
   prioritize the Skill Gaps first.

10. Give practical advice and examples.
"""

    # -----------------------------------------------------
    # Student Information
    # -----------------------------------------------------

    student_info = f"""

Student Name:
{name}

University:
{university}

Major:
{major}

University Year:
{year}

Current Skills:
{", ".join(current_skills)}

Original CV Skills:
{student_skills}

Interests:
{interests}

Favorite Subjects:
{favorite_subjects}

Work Style:
{work_style}

Experience Level:
{experience_level}

Recommended Career:
{career}

Match Score:
{score}%

Why This Career:
{reason}

Skill Gaps:
{", ".join(skill_gaps)}

Optional Future Skills:
{", ".join(optional_skills)}

Roadmap:
{" -> ".join(roadmap)}
"""

    # -----------------------------------------------------
    # Ask Gemini
    # -----------------------------------------------------

    try:

        response = client.chat.completions.create(

            model="google/gemini-2.5-flash",

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content":
                        f"""
Student Profile:

{student_info}

Student Question:

{request.question}
"""
                }
            ],

            max_tokens=1000,
        )

        answer = (
            response
            .choices[0]
            .message
            .content
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"AI Assistant Error: {str(e)}"
        )

    return {

        "student_id":
            request.student_id,

        "question":
            request.question,

        "career":
            career,

        "answer":
            answer,
    }


# =========================================================
# CV TEXT EXTRACTION
# =========================================================

def extract_cv_text(
    content: bytes,
    file_extension: str
):

    cv_text = ""

    # -----------------------------------------------------
    # PDF
    # -----------------------------------------------------

    if file_extension == ".pdf":

        pdf_file = io.BytesIO(
            content
        )

        reader = PdfReader(
            pdf_file
        )

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                cv_text += (
                    extracted + "\n"
                )

    # -----------------------------------------------------
    # DOCX
    # -----------------------------------------------------

    elif file_extension == ".docx":

        doc_file = io.BytesIO(
            content
        )

        document = Document(
            doc_file
        )

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                cv_text += (
                    paragraph.text + "\n"
                )

    # -----------------------------------------------------
    # TXT
    # -----------------------------------------------------

    elif file_extension == ".txt":

        cv_text = content.decode(
            "utf-8",
            errors="ignore"
        )

    # -----------------------------------------------------
    # Old DOC
    # -----------------------------------------------------

    elif file_extension == ".doc":

        raise HTTPException(
            status_code=400,
            detail=(
                "Old .doc files are not supported directly. "
                "Please save the CV as .docx or PDF and upload it again."
            )
        )

    return cv_text.strip()


# =========================================================
# AI CV SKILL EXTRACTION
# =========================================================

def extract_cv_profile(
    cv_text: str
):

    prompt = f"""
You are a CV information extraction system.

Analyze the CV below.

Your job is ONLY to extract information
that is explicitly present in the CV.

Do NOT recommend a career.

Do NOT calculate a score.

Do NOT invent skills.

Return ONLY valid JSON.

Use this exact structure:

{{
    "name": "",
    "university": "",
    "major": "",
    "year": 1,
    "skills": [],
    "interests": [],
    "projects": [],
    "experience": [],
    "experience_level": ""
}}

Rules:

- "skills" must contain only skills
  explicitly mentioned in the CV.

- "interests" must contain only interests
  explicitly mentioned.

- "projects" must contain project names
  or short project descriptions.

- "experience" must contain actual
  work or internship experience.

- "experience_level" can be:
  "Beginner",
  "Intermediate",
  "Advanced",
  or "Not specified".

- If something is missing,
  use an empty string or empty list.

CV:

{cv_text[:10000]}
"""

    try:

        response = client.chat.completions.create(

            model="google/gemini-2.5-flash",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.1,

            max_tokens=1500,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"CV AI extraction error: {str(e)}"
        )

    if (
        not response.choices
        or not response.choices[0].message.content
    ):

        raise HTTPException(
            status_code=500,
            detail="AI returned an empty CV analysis."
        )

    raw_response = (
        response
        .choices[0]
        .message
        .content
        .strip()
    )

    # -----------------------------------------------------
    # Remove markdown JSON fences if Gemini adds them
    # -----------------------------------------------------

    if raw_response.startswith("```"):

        raw_response = (
            raw_response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

    # -----------------------------------------------------
    # Parse JSON
    # -----------------------------------------------------

    try:

        profile = json.loads(
            raw_response
        )

    except json.JSONDecodeError:

        raise HTTPException(
            status_code=500,
            detail=(
                "AI returned invalid CV data. "
                "Please try uploading the CV again."
            )
        )

    # -----------------------------------------------------
    # Validate structure
    # -----------------------------------------------------

    if not isinstance(profile, dict):

        raise HTTPException(
            status_code=500,
            detail="Invalid CV analysis format."
        )

    profile.setdefault(
        "name",
        ""
    )

    profile.setdefault(
        "university",
        ""
    )

    profile.setdefault(
        "major",
        ""
    )

    profile.setdefault(
        "year",
        1
    )

    profile.setdefault(
        "skills",
        []
    )

    profile.setdefault(
        "interests",
        []
    )

    profile.setdefault(
        "projects",
        []
    )

    profile.setdefault(
        "experience",
        []
    )

    profile.setdefault(
        "experience_level",
        "Not specified"
    )

    # Make sure skills are strings

    profile["skills"] = [
        str(skill).strip()
        for skill in profile["skills"]
        if str(skill).strip()
    ]

    profile["interests"] = [
        str(interest).strip()
        for interest in profile["interests"]
        if str(interest).strip()
    ]

    return profile


# =========================================================
# SAVE CV STUDENT
# =========================================================

def save_cv_student(
    profile
):

    connection = get_connection()
    cursor = connection.cursor()

    name = (
        profile.get("name")
        or "CV Candidate"
    )

    university = (
        profile.get("university")
        or "Not specified"
    )

    major = (
        profile.get("major")
        or "Not specified"
    )

    year = profile.get(
        "year",
        1
    )

    try:

        year = int(year)

    except Exception:

        year = 1

    if year < 1:

        year = 1

    skills = profile.get(
        "skills",
        []
    )

    skills_text = ", ".join(
        skills
    )

    cursor.execute(
        """
        INSERT INTO students
        (name, university, major, year, skills)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            name,
            university,
            major,
            year,
            skills_text,
        ),
    )

    connection.commit()

    student_id = cursor.lastrowid

    # -----------------------------------------------------
    # Create assessment from CV
    # -----------------------------------------------------

    interests = profile.get(
        "interests",
        []
    )

    cursor.execute(
        """
        INSERT INTO assessments
        (
            student_id,
            interests,
            favorite_subjects,
            work_style,
            experience_level
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            student_id,

            ", ".join(interests),

            "",

            "",

            profile.get(
                "experience_level",
                "Not specified"
            ),
        ),
    )

    connection.commit()

    connection.close()

    return student_id


# =========================================================
# ANALYZE CV
# =========================================================

@app.post("/analyze-cv")
async def analyze_cv(
    file: UploadFile = File(...)
):

    # -----------------------------------------------------
    # Check filename
    # -----------------------------------------------------

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="Please upload a file."
        )

    file_extension = os.path.splitext(
        file.filename
    )[1].lower()

    allowed_extensions = [
        ".pdf",
        ".docx",
        ".txt"
    ]

    if file_extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail=(
                "Please upload a PDF, DOCX, "
                "or TXT file."
            )
        )

    # -----------------------------------------------------
    # Read file
    # -----------------------------------------------------

    try:

        content = await file.read()

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Could not read the uploaded file."
        )

    # -----------------------------------------------------
    # Check size
    # -----------------------------------------------------

    max_size = 10 * 1024 * 1024

    if len(content) > max_size:

        raise HTTPException(
            status_code=400,
            detail="File size must be less than 10MB."
        )

    if len(content) == 0:

        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty."
        )

    # -----------------------------------------------------
    # Extract CV text
    # -----------------------------------------------------

    try:

        cv_text = extract_cv_text(
            content,
            file_extension
        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=(
                f"Could not extract CV text: {str(e)}"
            )
        )

    # -----------------------------------------------------
    # Empty CV
    # -----------------------------------------------------

    if not cv_text.strip():

        raise HTTPException(
            status_code=400,
            detail=(
                "Could not extract text from this CV. "
                "If it is a scanned/image PDF, "
                "please upload a text-based PDF or DOCX."
            )
        )

    # -----------------------------------------------------
    # STEP 1:
    # Gemini extracts CV information
    # -----------------------------------------------------

    profile = extract_cv_profile(
        cv_text
    )

    extracted_skills = profile.get(
        "skills",
        []
    )

    interests = profile.get(
        "interests",
        []
    )

    # -----------------------------------------------------
    # STEP 2:
    # Save student
    # -----------------------------------------------------

    student_id = save_cv_student(
        profile
    )

    # -----------------------------------------------------
    # STEP 3:
    # CareerMate deterministic engine
    # -----------------------------------------------------

    result = ai_recommend_career(

        skills=extracted_skills,

        interests=interests,

        favorite_subjects=[],

        work_style="",

        experience_level=
            profile.get(
                "experience_level",
                ""
            ),
    )

    # -----------------------------------------------------
    # STEP 4:
    # Return complete analysis
    # -----------------------------------------------------

    return {

        "student_id":
            student_id,

        "file_name":
            file.filename,

        "candidate_name":
            profile.get(
                "name",
                ""
            ),

        "recommended_career":
            result["career"],

        "match_score":
            result["score"],

        "reason":
            result["reason"],

        "current_skills":
            result["current_skills"],

        "skill_gaps":
            result["skill_gaps"],

        "skills_to_learn":
            result["skills_to_learn"],

        "optional_skills":
            result["optional_skills"],

        "roadmap":
            result["roadmap"],

        "top_recommendations":
            result["top_recommendations"],

        "projects":
            profile.get(
                "projects",
                []
            ),

        "experience":
            profile.get(
                "experience",
                []
            ),

        "message":
            "CV analyzed successfully",
    }


# =========================================================
# FRONTEND
# =========================================================

app.mount(
    "/frontend",
    StaticFiles(
        directory="frontend",
        html=True
    ),
    name="frontend"
)