
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# CAREER DESCRIPTIONS
# =========================================================

careers = {

    "Frontend Developer":
        "HTML CSS JavaScript React TypeScript UI web development frontend websites responsive design",

    "Backend Developer":
        "Python FastAPI Django Node.js SQL APIs databases server backend development authentication",

    "Full Stack Developer":
        "HTML CSS JavaScript React Python Node.js SQL APIs frontend backend full stack web development",

    "Mobile App Developer":
        "Android iOS Flutter React Native Kotlin Swift mobile applications app development",

    "AI Engineer":
        "Python artificial intelligence AI machine learning deep learning neural networks TensorFlow PyTorch",

    "Data Scientist":
        "Python pandas numpy statistics machine learning data science data analysis visualization",

    "Data Analyst":
        "Excel SQL Python Power BI Tableau data analysis statistics dashboards reports business intelligence",

    "Cybersecurity Engineer":
        "security networks Linux cybersecurity ethical hacking penetration testing protection vulnerabilities",

    "Cloud / DevOps Engineer":
        "AWS Azure cloud DevOps Docker Kubernetes Linux CI CD deployment infrastructure automation",

    "Software QA Engineer":
        "software testing QA quality assurance manual testing automation Selenium test cases debugging",

    "UI/UX Designer":
        "UI UX design Figma user experience user interface wireframes prototypes research creativity",

    "Game Developer":
        "C++ C# Unity Unreal Engine game development gaming graphics physics programming",

    "Database Administrator":
        "SQL databases MySQL PostgreSQL Oracle database administration data backup optimization",

    "Blockchain Developer":
        "blockchain cryptocurrency Ethereum Solidity smart contracts Web3 decentralized applications",

    "Computer Vision Engineer":
        "Python OpenCV computer vision image processing deep learning object detection images AI",

    "NLP / Generative AI Engineer":
        "Python NLP natural language processing LLM generative AI ChatGPT transformers language models text"
}

career_work_styles = {

    "Frontend Developer": [
        "Creative",
        "Teamwork"
    ],

    "Backend Developer": [
        "Analytical",
        "Independent"
    ],

    "Full Stack Developer": [
        "Teamwork",
        "Analytical"
    ],

    "Mobile App Developer": [
        "Creative",
        "Teamwork"
    ],

    "AI Engineer": [
        "Analytical",
        "Independent"
    ],

    "Data Scientist": [
        "Analytical",
        "Independent"
    ],

    "Data Analyst": [
        "Analytical",
        "Teamwork"
    ],

    "Cybersecurity Engineer": [
        "Analytical",
        "Independent"
    ],

    "Cloud / DevOps Engineer": [
        "Analytical",
        "Independent"
    ],

    "Software QA Engineer": [
        "Analytical",
        "Teamwork"
    ],

    "UI/UX Designer": [
        "Creative",
        "Teamwork"
    ],

    "Game Developer": [
        "Creative",
        "Independent"
    ],

    "Database Administrator": [
        "Analytical",
        "Independent"
    ],

    "Blockchain Developer": [
        "Analytical",
        "Independent"
    ],

    "Computer Vision Engineer": [
        "Analytical",
        "Independent"
    ],

    "NLP / Generative AI Engineer": [
        "Analytical",
        "Creative"
    ]
}

# =========================================================
# SKILLS TO LEARN
# =========================================================

skills_to_learn = {

    "Frontend Developer": [
        "React",
        "TypeScript",
        "Git",
        "Responsive Design"
    ],

    "Backend Developer": [
        "Python",
        "FastAPI",
        "SQL",
        "REST APIs",
        "Docker"
    ],

    "Full Stack Developer": [
        "HTML & CSS",
        "JavaScript",
        "React",
        "Node.js",
        "SQL",
        "REST APIs",
        "Git"
    ],

    "Mobile App Developer": [
        "Flutter",
        "Dart",
        "Mobile UI Design",
        "APIs",
        "Firebase"
    ],

    "AI Engineer": [
        "Python",
        "NumPy",
        "Pandas",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow"
    ],

    "Data Scientist": [
        "Python",
        "Pandas",
        "NumPy",
        "Statistics",
        "Data Visualization",
        "Machine Learning"
    ],

    "Data Analyst": [
        "Excel",
        "SQL",
        "Power BI",
        "Python",
        "Statistics",
        "Data Visualization"
    ],

    "Cybersecurity Engineer": [
        "Linux",
        "Networking",
        "Cybersecurity Basics",
        "Ethical Hacking",
        "Penetration Testing"
    ],

    "Cloud / DevOps Engineer": [
        "Linux",
        "Git",
        "Docker",
        "AWS",
        "Kubernetes",
        "CI/CD"
    ],

    "Software QA Engineer": [
        "Software Testing",
        "Test Cases",
        "Selenium",
        "API Testing",
        "Automation Testing"
    ],

    "UI/UX Designer": [
        "Figma",
        "Wireframing",
        "Prototyping",
        "User Research",
        "Design Systems"
    ],

    "Game Developer": [
        "C++",
        "C#",
        "Unity",
        "Unreal Engine",
        "Game Physics"
    ],

    "Database Administrator": [
        "SQL",
        "MySQL",
        "PostgreSQL",
        "Database Security",
        "Backup & Recovery",
        "Query Optimization"
    ],

    "Blockchain Developer": [
        "Blockchain Basics",
        "Solidity",
        "Ethereum",
        "Smart Contracts",
        "Web3"
    ],

    "Computer Vision Engineer": [
        "Python",
        "OpenCV",
        "NumPy",
        "Computer Vision",
        "Deep Learning",
        "Object Detection"
    ],

    "NLP / Generative AI Engineer": [
        "Python",
        "NLP",
        "Transformers",
        "LLMs",
        "Prompt Engineering",
        "Generative AI"
    ]
}


# =========================================================
# LEARNING ROADMAPS
# =========================================================

roadmaps = {

    "Frontend Developer": [
        "Learn HTML and CSS",
        "Learn JavaScript",
        "Learn React",
        "Learn TypeScript",
        "Build responsive websites",
        "Learn Git and GitHub",
        "Build real frontend projects"
    ],

    "Backend Developer": [
        "Learn Python",
        "Learn FastAPI or Django",
        "Learn SQL and databases",
        "Build REST APIs",
        "Learn authentication",
        "Learn Docker",
        "Build backend projects"
    ],

    "Full Stack Developer": [
        "Learn HTML and CSS",
        "Learn JavaScript",
        "Learn React",
        "Learn backend development",
        "Learn SQL",
        "Build REST APIs",
        "Connect frontend with backend",
        "Build full stack projects"
    ],

    "Mobile App Developer": [
        "Learn Dart or Kotlin",
        "Learn Flutter or Android Development",
        "Learn mobile UI design",
        "Learn APIs",
        "Learn Firebase",
        "Build mobile applications",
        "Publish a real app"
    ],

    "AI Engineer": [
        "Learn Python",
        "Learn NumPy and Pandas",
        "Learn Machine Learning",
        "Learn Deep Learning",
        "Learn TensorFlow or PyTorch",
        "Learn Neural Networks",
        "Build AI projects"
    ],

    "Data Scientist": [
        "Learn Python",
        "Learn Pandas and NumPy",
        "Learn Statistics",
        "Learn Data Visualization",
        "Learn Machine Learning",
        "Practice with real datasets",
        "Build data science projects"
    ],

    "Data Analyst": [
        "Learn Excel",
        "Learn SQL",
        "Learn Statistics",
        "Learn Power BI or Tableau",
        "Learn Python for Data Analysis",
        "Build dashboards",
        "Analyze real datasets"
    ],

    "Cybersecurity Engineer": [
        "Learn Linux",
        "Learn Computer Networks",
        "Learn Cybersecurity Basics",
        "Learn Python for Security",
        "Learn Ethical Hacking",
        "Practice penetration testing",
        "Build security projects"
    ],

    "Cloud / DevOps Engineer": [
        "Learn Linux",
        "Learn Git and GitHub",
        "Learn Docker",
        "Learn AWS or Azure",
        "Learn CI/CD",
        "Learn Kubernetes",
        "Deploy real applications"
    ],

    "Software QA Engineer": [
        "Learn Software Testing Basics",
        "Learn Test Cases",
        "Learn Bug Reporting",
        "Learn API Testing",
        "Learn Selenium",
        "Learn Automation Testing",
        "Build a testing portfolio"
    ],

    "UI/UX Designer": [
        "Learn UI/UX principles",
        "Learn Figma",
        "Learn Wireframing",
        "Learn Prototyping",
        "Learn User Research",
        "Create design systems",
        "Build a UI/UX portfolio"
    ],

    "Game Developer": [
        "Learn C++ or C#",
        "Learn Unity or Unreal Engine",
        "Learn Game Physics",
        "Learn 2D/3D Game Development",
        "Learn Game Design",
        "Build small games",
        "Publish a complete game"
    ],

    "Database Administrator": [
        "Learn SQL",
        "Learn MySQL or PostgreSQL",
        "Learn Database Design",
        "Learn Database Security",
        "Learn Backup and Recovery",
        "Learn Query Optimization",
        "Manage real databases"
    ],

    "Blockchain Developer": [
        "Learn Blockchain Basics",
        "Learn Ethereum",
        "Learn Solidity",
        "Learn Smart Contracts",
        "Learn Web3",
        "Build decentralized applications",
        "Deploy a blockchain project"
    ],

    "Computer Vision Engineer": [
        "Learn Python",
        "Learn NumPy",
        "Learn OpenCV",
        "Learn Image Processing",
        "Learn Deep Learning",
        "Learn Object Detection",
        "Build computer vision projects"
    ],

    "NLP / Generative AI Engineer": [
        "Learn Python",
        "Learn NLP Basics",
        "Learn Transformers",
        "Learn Large Language Models",
        "Learn Prompt Engineering",
        "Learn Generative AI",
        "Build AI applications"
    ]
}


# =========================================================
# PREPARE CAREER DATA
# =========================================================

career_names = list(careers.keys())
career_descriptions = list(careers.values())

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words=None
)

career_vectors = vectorizer.fit_transform(career_descriptions)


# =========================================================
# CAREER RECOMMENDATION
# =========================================================

def recommend_career(
    skills,
    interests,
    favorite_subjects,
    work_style="",
    experience_level=""
):
    # Make sure inputs are lists
    skills = skills or []
    interests = interests or []
    favorite_subjects = favorite_subjects or []

    # Convert everything to strings
    skills = [str(x) for x in skills]
    interests = [str(x) for x in interests]
    favorite_subjects = [str(x) for x in favorite_subjects]

    # Combine student information
    student_text = " ".join(
        skills + interests + favorite_subjects
    )

    # Convert student data to TF-IDF vector
    student_vector = vectorizer.transform([student_text])

    # Calculate similarity
    similarities = cosine_similarity(
        student_vector,
        career_vectors
    )[0]

    # Calculate work style score
    work_style_scores = []

    for career in career_names:
        preferred_styles = career_work_styles.get(career, [])

        if work_style in preferred_styles:
            work_style_scores.append(1.0)
        else:
            work_style_scores.append(0.0)

    # =====================================================
    # CALCULATE FINAL SCORES
    # =====================================================

    final_scores = []

    for i in range(len(career_names)):

        tfidf_score = float(similarities[i])
        work_score = work_style_scores[i]

        final_score = (
            tfidf_score * 0.90
            +
            work_score * 0.10
        )

        final_scores.append(final_score)

    # =====================================================
    # RANK ALL CAREERS
    # =====================================================

    ranked_indexes = sorted(
        range(len(career_names)),
        key=lambda i: final_scores[i],
        reverse=True
    )

    recommendations = []

    for index in ranked_indexes[:3]:

        career = career_names[index]

        recommendations.append({
            "career": career,
            "score": round(
                float(final_scores[index]) * 100,
                2
            )
        })

    # Best career
    best_index = ranked_indexes[0]
    best_career = career_names[best_index]

    best_score = round(
        float(final_scores[best_index]) * 100,
        2
    )

    # =====================================================
    # NORMALIZE STUDENT SKILLS
    # =====================================================

    student_skills = {
        skill.strip().lower()
        for skill in skills
    }

    # =====================================================
    # FILTER SKILLS TO LEARN
    # =====================================================

    remaining_skills = [
        skill
        for skill in skills_to_learn[best_career]
        if skill.lower() not in student_skills
    ]

    # =====================================================
    # SMART ROADMAP
    # =====================================================

    filtered_roadmap = []

    for step in roadmaps[best_career]:

        step_lower = step.lower()

        # HTML + CSS
        if "html" in step_lower and "css" in step_lower:

            if (
                "html" not in student_skills
                and "css" not in student_skills
            ):
                filtered_roadmap.append(step)

            elif "html" not in student_skills:
                filtered_roadmap.append("Learn HTML")

            elif "css" not in student_skills:
                filtered_roadmap.append("Learn CSS")

            continue

        # Check if any known skill exists in roadmap step
        already_known = any(
            skill in step_lower
            for skill in student_skills
        )

        if not already_known:
            filtered_roadmap.append(step)

    # =====================================================
    # RETURN RESULT
    # =====================================================

    return {
        "career": best_career,
        "score": best_score,
        "reason": (
            f"Your skills, interests, and favorite subjects "
            f"match well with {best_career}."
        ),
        "skills_to_learn": remaining_skills,
        "roadmap": filtered_roadmap,
        "top_recommendations": recommendations
    }
    # =====================================================
    # RANK ALL CAREERS
    # =====================================================

    ranked_indexes = sorted(
        range(len(career_names)),
        key=lambda i: final_scores[i],
        reverse=True
    )
    recommendations = []

    for index in ranked_indexes[:3]:

        career = career_names[index]

        recommendations.append({
            "career": career,
            "score": round(
                float(final_scores[index]) * 100,
                2
            )
        })

    # Best career
    best_index = ranked_indexes[0]
    best_career = career_names[best_index]
    best_score = round(
        float(final_scores[best_index]) * 100,
        2
    )

    # =====================================================
    # NORMALIZE STUDENT SKILLS
    # =====================================================

    student_skills = {
        skill.strip().lower()
        for skill in skills
    }

    # =====================================================
    # FILTER SKILLS TO LEARN
    # =====================================================

    remaining_skills = [
        skill
        for skill in skills_to_learn[best_career]
        if skill.lower() not in student_skills
    ]

    # =====================================================
    # SMART ROADMAP
    # =====================================================

    filtered_roadmap = []

    for step in roadmaps[best_career]:

        step_lower = step.lower()

        # HTML + CSS
        if "html" in step_lower and "css" in step_lower:

            if (
                "html" not in student_skills
                and "css" not in student_skills
            ):
                filtered_roadmap.append(step)

            elif "html" not in student_skills:
                filtered_roadmap.append("Learn HTML")

            elif "css" not in student_skills:
                filtered_roadmap.append("Learn CSS")

            continue

        # Check if any known skill exists in roadmap step
        already_known = any(
            skill in step_lower
            for skill in student_skills
        )

        if not already_known:
            filtered_roadmap.append(step)

    # =====================================================
    # RETURN RESULT
    # =====================================================

    return {

        # Existing fields - frontend remains compatible
        "career": best_career,

        "score": best_score,

        "reason": (
            f"Your skills, interests, and favorite subjects "
            f"match well with {best_career}."
        ),

        "skills_to_learn": remaining_skills,

        "roadmap": filtered_roadmap,

        # New field
        "top_recommendations": recommendations
    }


# =========================================================
# TEST THE AI
# =========================================================

if __name__ == "__main__":

    result = recommend_career(

        skills=[
            "Python",
            "Pandas",
            "NumPy"
        ],

        interests=[
            "Data Analysis",
            "Machine Learning"
        ],

        favorite_subjects=[
            "Mathematics",
            "Programming"
        ]
    )

    print("\n==============================")
    print("BEST CAREER")
    print("==============================")

    print(result["career"])
    print("Score:", result["score"], "%")

    print("\n==============================")
    print("TOP 3 CAREERS")
    print("==============================")

    for recommendation in result["top_recommendations"]:
        print(
            recommendation["career"],
            "-",
            recommendation["score"],
            "%"
        )

    print("\n==============================")
    print("SKILLS TO LEARN")
    print("==============================")

    for skill in result["skills_to_learn"]:
        print("-", skill)

    print("\n==============================")
    print("ROADMAP")
    print("==============================")

    for step in result["roadmap"]:
        print("-", step)

