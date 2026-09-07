from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from career_model import recommend_career as ai_recommend_career
app = FastAPI(title="CareerMate AI")


# =========================
# Database Setup
# =========================

def get_connection():
    connection = sqlite3.connect("careermate.db")
    connection.row_factory = sqlite3.Row
    return connection


connection = get_connection()
cursor = connection.cursor()

# Students Table
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

# Assessments Table
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


# =========================
# Student Model
# =========================

class StudentProfile(BaseModel):
    name: str
    university: str
    major: str
    year: int
    skills: list[str]


# =========================
# Career Assessment Model
# =========================

class CareerAssessment(BaseModel):
    student_id: int
    interests: list[str]
    favorite_subjects: list[str]
    work_style: str
    experience_level: str


# =========================
# Home
# =========================

@app.get("/")
def home():
    return {
        "message": "CareerMate AI is running!"
    }


# =========================
# Create Student
# =========================

@app.post("/students")
def create_student(student: StudentProfile):

    connection = get_connection()
    cursor = connection.cursor()

    skills_text = ", ".join(student.skills)

    cursor.execute("""
    INSERT INTO students (name, university, major, year, skills)
    VALUES (?, ?, ?, ?, ?)
    """, (
        student.name,
        student.university,
        student.major,
        student.year,
        skills_text
    ))

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
            "skills": student.skills
        }
    }


# =========================
# Get All Students
# =========================

@app.get("/students")
def get_students():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return {
        "students": [dict(student) for student in students]
    }


# =========================
# Get Student By ID
# =========================

@app.get("/students/{student_id}")
def get_student(student_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
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


# =========================
# Create Career Assessment
# =========================

@app.post("/assessment")
def create_assessment(assessment: CareerAssessment):

    connection = get_connection()
    cursor = connection.cursor()

    # Check if student exists
    cursor.execute(
        "SELECT id FROM students WHERE id = ?",
        (assessment.student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    interests_text = ", ".join(assessment.interests)
    subjects_text = ", ".join(assessment.favorite_subjects)

    cursor.execute("""
    INSERT INTO assessments (
        student_id,
        interests,
        favorite_subjects,
        work_style,
        experience_level
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        assessment.student_id,
        interests_text,
        subjects_text,
        assessment.work_style,
        assessment.experience_level
    ))

    connection.commit()

    assessment_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Career assessment created successfully",
        "assessment_id": assessment_id,
        "assessment": {
            "student_id": assessment.student_id,
            "interests": assessment.interests,
            "favorite_subjects": assessment.favorite_subjects,
            "work_style": assessment.work_style,
            "experience_level": assessment.experience_level
        }
    }


# =========================
# Get All Assessments
# =========================

@app.get("/assessments")
def get_assessments():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM assessments")
    assessments = cursor.fetchall()

    connection.close()

    return {
        "assessments": [dict(assessment) for assessment in assessments]
    }


# =========================
# Get Assessment By Student ID
# =========================

@app.get("/students/{student_id}/assessment")
def get_student_assessment(student_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM assessments
    WHERE student_id = ?
    ORDER BY id DESC
    LIMIT 1
    """, (student_id,))

    assessment = cursor.fetchone()

    connection.close()

    if assessment is None:
        raise HTTPException(
            status_code=404,
            detail="Assessment not found for this student"
        )

    return {
        "assessment": dict(assessment)
    }
class CareerRecommendationRequest(BaseModel):
    student_id: int
    # =========================
# Career Recommendation
# =========================
@app.post("/recommend")
def recommend_career(request: CareerRecommendationRequest):

    connection = get_connection()
    cursor = connection.cursor()

    # Get student
    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (request.student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Get latest assessment
    cursor.execute("""
    SELECT *
    FROM assessments
    WHERE student_id = ?
    ORDER BY id DESC
    LIMIT 1
    """, (request.student_id,))

    assessment = cursor.fetchone()

    connection.close()

    if assessment is None:
        raise HTTPException(
            status_code=404,
            detail="Assessment not found for this student"
        )

    # Convert database data to lists
    skills = [
        skill.strip()
        for skill in student["skills"].split(",")
    ]

    interests = [
        interest.strip()
        for interest in assessment["interests"].split(",")
    ]

    favorite_subjects = [
        subject.strip()
        for subject in assessment["favorite_subjects"].split(",")
    ]

    # Use AI model
    result = ai_recommend_career(
        skills=skills,
        interests=interests,
        favorite_subjects=favorite_subjects
    )

    return {
        "student_id": request.student_id,
        "recommended_career": result["career"],
        "match_score": result["score"],
        "reason": result["reason"],
        "skills_to_learn": result["skills_to_learn"],
        "roadmap": result["roadmap"],
        "message": "AI career recommendation generated successfully"
    }