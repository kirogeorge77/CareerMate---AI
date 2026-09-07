import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Career descriptions
careers = {
    "Frontend Developer": "HTML CSS JavaScript React UI web development",
    "Backend Developer": "Python FastAPI SQL APIs databases backend development",
    "AI Engineer": "Python machine learning artificial intelligence deep learning data",
    "Data Scientist": "Python pandas numpy statistics machine learning data analysis",
    "Cybersecurity Engineer": "security networks Linux cybersecurity ethical hacking protection"
}


# Skills the student should learn
skills_to_learn = {
    "Frontend Developer": [
        "React",
        "TypeScript",
        "Git",
        "Responsive Design"
    ],
    "Backend Developer": [
        "FastAPI",
        "SQL",
        "REST APIs",
        "Docker"
    ],
    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow"
    ],
    "Data Scientist": [
        "Python",
        "Pandas",
        "NumPy",
        "Statistics",
        "Machine Learning"
    ],
    "Cybersecurity Engineer": [
        "Linux",
        "Networking",
        "Cybersecurity Basics",
        "Ethical Hacking"
    ]
}


# Learning roadmap
roadmaps = {
    "Frontend Developer": [
        "Learn HTML and CSS",
        "Learn JavaScript",
        "Learn React",
        "Learn TypeScript",
        "Build real projects",
        "Learn Git and GitHub"
    ],
    "Backend Developer": [
        "Learn Python",
        "Learn FastAPI",
        "Learn SQL and databases",
        "Build REST APIs",
        "Learn Docker",
        "Build backend projects"
    ],
    "AI Engineer": [
        "Learn Python",
        "Learn NumPy and Pandas",
        "Learn Machine Learning",
        "Learn Deep Learning",
        "Learn TensorFlow",
        "Build AI projects"
    ],
    "Data Scientist": [
        "Learn Python",
        "Learn Pandas and NumPy",
        "Learn Statistics",
        "Learn Data Visualization",
        "Learn Machine Learning",
        "Work on real datasets"
    ],
    "Cybersecurity Engineer": [
        "Learn Linux",
        "Learn Computer Networks",
        "Learn Cybersecurity Basics",
        "Learn Ethical Hacking",
        "Practice on security labs",
        "Build security projects"
    ]
}


# Prepare career data
career_names = list(careers.keys())
career_descriptions = list(careers.values())

vectorizer = TfidfVectorizer()
career_vectors = vectorizer.fit_transform(career_descriptions)


# Career recommendation function
def recommend_career(skills, interests, favorite_subjects):
    student_text = " ".join(
        skills + interests + favorite_subjects
    )

    student_vector = vectorizer.transform([student_text])

    similarities = cosine_similarity(
        student_vector,
        career_vectors
    )[0]

    best_index = similarities.argmax()
    best_career = career_names[best_index]

    return {
        "career": best_career,
        "score": round(
            float(similarities[best_index]) * 100,
            2
        ),
        "reason": (
            f"Your skills and interests match well "
            f"with {best_career}."
        ),
        "skills_to_learn": skills_to_learn[best_career],
        "roadmap": roadmaps[best_career]
    }


# Test the AI
if __name__ == "__main__":
    result = recommend_career(
        skills=[
            "HTML",
            "CSS",
            "JavaScript"
        ],
        interests=[
            "Web Development"
        ],
        favorite_subjects=[
            "Programming"
        ]
    )

    print(result)