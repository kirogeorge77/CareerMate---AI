from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# CAREER DESCRIPTIONS
# =========================================================

careers = {
    "Frontend Developer":
        "HTML CSS JavaScript React TypeScript UI web development frontend websites responsive design REST APIs Git",

    "Backend Developer":
        "Python FastAPI Django Node.js SQL APIs databases server backend development authentication Docker",

    "Full Stack Developer":
        "HTML CSS JavaScript React Python Node.js SQL APIs frontend backend full stack web development Git",

    "Mobile App Developer":
        "Android iOS Flutter React Native Kotlin Swift mobile applications app development Firebase",

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
        "software testing QA quality assurance manual testing automation Selenium test cases debugging API testing",

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


# =========================================================
# CAREER WORK STYLES
# =========================================================

career_work_styles = {

    "Frontend Developer": ["Creative", "Teamwork"],
    "Backend Developer": ["Analytical", "Independent"],
    "Full Stack Developer": ["Teamwork", "Analytical"],
    "Mobile App Developer": ["Creative", "Teamwork"],
    "AI Engineer": ["Analytical", "Independent"],
    "Data Scientist": ["Analytical", "Independent"],
    "Data Analyst": ["Analytical", "Teamwork"],
    "Cybersecurity Engineer": ["Analytical", "Independent"],
    "Cloud / DevOps Engineer": ["Analytical", "Independent"],
    "Software QA Engineer": ["Analytical", "Teamwork"],
    "UI/UX Designer": ["Creative", "Teamwork"],
    "Game Developer": ["Creative", "Independent"],
    "Database Administrator": ["Analytical", "Independent"],
    "Blockchain Developer": ["Analytical", "Independent"],
    "Computer Vision Engineer": ["Analytical", "Independent"],
    "NLP / Generative AI Engineer": ["Analytical", "Creative"]
}


# =========================================================
# CAREER REQUIRED SKILLS
# =========================================================

career_requirements = { 


    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "TypeScript",
        "Git",
        "Responsive Design",
        "REST APIs"
    ],

    "Backend Developer": [
        "Python",
        "FastAPI",
        "SQL",
        "REST APIs",
        "Databases",
        "Authentication",
        "Docker"
    ],

    "Full Stack Developer": [
        "HTML",
        "CSS",
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
        "Firebase",
        "REST APIs",
        "Mobile UI Design"
    ],

    "AI Engineer": [
        "Python",
        "NumPy",
        "Pandas",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch"
    ],

    "Data Scientist": [
        "Python",
        "Pandas",
        "NumPy",
        "Statistics",
        "Machine Learning",
        "Data Visualization"
    ],

    "Data Analyst": [
        "Excel",
        "SQL",
        "Python",
        "Statistics",
        "Power BI",
        "Data Visualization"
    ],

    "Cybersecurity Engineer": [
        "Linux",
        "Networking",
        "Cybersecurity",
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
        "Bug Reporting",
        "API Testing",
        "Selenium",
        "Automation Testing"
    ],

    "UI/UX Designer": [
        "Figma",
        "UI Design",
        "UX Design",
        "Wireframing",
        "Prototyping",
        "User Research"
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
        "Database Design",
        "Database Security",
        "Query Optimization"
    ],

    "Blockchain Developer": [
        "Blockchain",
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
# CORE SKILLS
# =========================================================

career_core_skills = {

    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React"
    ],

    "Backend Developer": [
        "Python",
        "FastAPI",
        "SQL",
        "REST APIs"
    ],

    "Full Stack Developer": [
        "React",
        "Node.js",
        "SQL",
        "REST APIs"
    ],

    "Mobile App Developer": [
        "Flutter",
        "Dart",
        "Firebase"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning"
    ],

    "Data Scientist": [
        "Python",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ],

    "Data Analyst": [
        "Excel",
        "SQL",
        "Power BI"
    ],

    "Cybersecurity Engineer": [
        "Linux",
        "Networking",
        "Cybersecurity"
    ],

    "Cloud / DevOps Engineer": [
        "Linux",
        "Docker",
        "AWS"
    ],

    "Software QA Engineer": [
        "Software Testing",
        "Test Cases",
        "Automation Testing"
    ],

    "UI/UX Designer": [
        "Figma",
        "UI Design",
        "UX Design"
    ],

    "Game Developer": [
        "C++",
        "C#",
        "Unity"
    ],

    "Database Administrator": [
        "SQL",
        "MySQL",
        "PostgreSQL"
    ],

    "Blockchain Developer": [
        "Blockchain",
        "Solidity",
        "Smart Contracts"
    ],

    "Computer Vision Engineer": [
        "Python",
        "OpenCV",
        "Computer Vision"
    ],

    "NLP / Generative AI Engineer": [
        "Python",
        "NLP",
        "LLMs"
    ]
}

# =========================================================
# OPTIONAL FUTURE SKILLS
# =========================================================

optional_skills = {

    "Frontend Developer": [
        "Node.js",
        "SQL",
        "Docker"
    ],

    "Backend Developer": [
        "React",
        "TypeScript",
        "Cloud"
    ],

    "Full Stack Developer": [
        "Docker",
        "AWS",
        "TypeScript"
    ],

    "Mobile App Developer": [
        "Kotlin",
        "Swift",
        "App Store Deployment"
    ],

    "AI Engineer": [
        "MLOps",
        "LLMs",
        "Computer Vision"
    ],

    "Data Scientist": [
        "Deep Learning",
        "MLOps",
        "Big Data"
    ],

    "Data Analyst": [
        "Machine Learning",
        "Power BI",
        "Cloud"
    ],

    "Cybersecurity Engineer": [
        "Cloud Security",
        "Digital Forensics",
        "Security Automation"
    ],

    "Cloud / DevOps Engineer": [
        "Terraform",
        "Ansible",
        "Cloud Security"
    ],

    "Software QA Engineer": [
        "Performance Testing",
        "CI/CD",
        "Docker"
    ],

    "UI/UX Designer": [
        "Design Systems",
        "Motion Design",
        "UX Writing"
    ],

    "Game Developer": [
        "3D Modeling",
        "Game AI",
        "Multiplayer Development"
    ],

    "Database Administrator": [
        "Cloud Databases",
        "Database Automation",
        "Big Data"
    ],

    "Blockchain Developer": [
        "DeFi",
        "NFT Development",
        "Blockchain Security"
    ],

    "Computer Vision Engineer": [
        "YOLO",
        "Image Segmentation",
        "MLOps"
    ],

    "NLP / Generative AI Engineer": [
        "RAG",
        "Vector Databases",
        "AI Agents"
    ]
}


# =========================================================
# LEARNING ROADMAPS
# =========================================================

roadmaps = {

    "Frontend Developer": [
        "Strengthen HTML and CSS",
        "Master JavaScript",
        "Learn Responsive Design",
        "Learn React",
        "Learn REST APIs",
        "Learn TypeScript",
        "Learn Git and GitHub",
        "Build 2 strong frontend projects",
        "Improve your GitHub portfolio"
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
        "Strengthen HTML and CSS",
        "Master JavaScript",
        "Learn React",
        "Learn Node.js",
        "Learn SQL",
        "Build REST APIs",
        "Connect frontend with backend",
        "Learn authentication",
        "Build full stack projects"
    ],

    "Mobile App Developer": [
        "Learn Dart or Kotlin",
        "Learn Flutter or Android Development",
        "Learn mobile UI design",
        "Learn REST APIs",
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
# SKILL NORMALIZATION
# =========================================================

SKILL_ALIASES = {

    # =========================
    # WEB / FRONTEND
    # =========================

    "html": "html",
    "html5": "html",

    "css": "css",
    "css3": "css",

    "js": "javascript",
    "javascript": "javascript",
    "javascript es6": "javascript",
    "ecmascript": "javascript",

    "react": "react",
    "react.js": "react",
    "reactjs": "react",
    "react js": "react",

    "typescript": "typescript",
    "ts": "typescript",
    "typescript.js": "typescript",

    "responsive design": "responsive design",
    "responsive web design": "responsive design",
    "mobile responsive design": "responsive design",

    # =========================
    # BACKEND
    # =========================

    "python": "python",
    "python3": "python",

    "fastapi": "fastapi",
    "fast api": "fastapi",

    "flask": "flask",

    "node": "node.js",
    "nodejs": "node.js",
    "node.js": "node.js",
    "node js": "node.js",

    "django": "django",

    "rest api": "rest apis",
    "rest apis": "rest apis",
    "restful api": "rest apis",
    "restful apis": "rest apis",
    "rest api development": "rest apis",
    "api development": "rest apis",
    "apis": "rest apis",

    "authentication": "authentication",
    "user authentication": "authentication",
    "api authentication": "authentication",
    "jwt": "authentication",

    # =========================
    # DATABASES
    # =========================

    "sql": "sql",
    "sql server": "sql",

    "database": "databases",
    "databases": "databases",
    "database systems": "databases",
    "database management": "databases",
    "database management systems": "databases",
    "db": "databases",

    "database design": "databases",
    "database development": "databases",

    "mysql": "databases",
    "my sql": "databases",

    "postgresql": "databases",
    "postgres": "databases",
    "postgre sql": "databases",

    "sqlite": "databases",
    "sql lite": "databases",

    "mongodb": "mongodb",
    "mongo db": "mongodb",
    "mongo": "mongodb",

    # =========================
    # GIT / DEVELOPMENT TOOLS
    # =========================

    "git": "git",
    "git version control": "git",

    "github": "github",
    "git hub": "github",

    "gitlab": "gitlab",

    "docker": "docker",
    "docker containers": "docker",

    "kubernetes": "kubernetes",
    "k8s": "kubernetes",

    # =========================
    # PROGRAMMING / CS
    # =========================

    "c++": "c++",
    "cpp": "c++",
    "cplusplus": "c++",

    "c#": "c#",
    "c sharp": "c#",
    "csharp": "c#",

    "java": "java",

    "object oriented programming": "oop",
    "object-oriented programming": "oop",
    "object oriented": "oop",
    "oop": "oop",

    "data structures": "data structures",
    "data structure": "data structures",

    "algorithms": "algorithms",
    "algorithm": "algorithms",

    "problem solving": "problem solving",

    "debugging": "debugging",

    "software engineering": "software engineering",

    # =========================
    # AI / MACHINE LEARNING
    # =========================

    "machine learning": "machine learning",
    "machine-learning": "machine learning",
    "ml": "machine learning",
    "machine learning fundamentals": "machine learning",

    "deep learning": "deep learning",
    "deep-learning": "deep learning",
    "dl": "deep learning",

    "artificial intelligence": "artificial intelligence",
    "ai": "artificial intelligence",

    "generative ai": "generative ai",
    "gen ai": "generative ai",

    "llm": "llms",
    "llms": "llms",
    "large language models": "llms",

    "nlp": "nlp",
    "natural language processing": "nlp",

    "computer vision": "computer vision",
    "cv": "computer vision",

    "opencv": "opencv",
    "open cv": "opencv",

    "pytorch": "pytorch",
    "py torch": "pytorch",

    "tensorflow": "tensorflow",
    "tensor flow": "tensorflow",

    # =========================
    # DATA SCIENCE / DATA ANALYSIS
    # =========================

    "numpy": "numpy",
    "num py": "numpy",

    "pandas": "pandas",

    "scikit-learn": "scikit-learn",
    "scikit learn": "scikit-learn",
    "sklearn": "scikit-learn",

    "matplotlib": "matplotlib",

    "seaborn": "seaborn",

    "jupyter": "jupyter",
    "jupyter notebook": "jupyter",

    "data analysis": "data analysis",
    "data analytics": "data analysis",

    "data visualization": "data visualization",
    "data visualisation": "data visualization",

    "statistics": "statistics",
    "statistical analysis": "statistics",

    "excel": "excel",
    "microsoft excel": "excel",

    "power bi": "power bi",
    "powerbi": "power bi",

    "tableau": "tableau",

    # =========================
    # CLOUD / DEVOPS
    # =========================

    "cloud computing": "cloud",
    "cloud": "cloud",

    "aws": "aws",
    "amazon web services": "aws",

    "azure": "azure",
    "microsoft azure": "azure",

    "google cloud": "google cloud",
    "gcp": "google cloud",

    "linux": "linux",
    "linux administration": "linux",

    "networking": "networking",
    "computer networks": "networking",
    "computer networking": "networking",
    "networks": "networking",

    "devops": "devops",

    # =========================
    # CYBERSECURITY
    # =========================

    "cybersecurity": "cybersecurity",
    "cyber security": "cybersecurity",
    "information security": "cybersecurity",
    "infosec": "cybersecurity",

    "ethical hacking": "ethical hacking",
    "penetration testing": "penetration testing",
    "pentesting": "penetration testing",

    # =========================
    # MOBILE DEVELOPMENT
    # =========================

    "flutter": "flutter",
    "flutter development": "flutter",

    "dart": "dart",

    "firebase": "firebase",

    "react native": "react native",
    "react-native": "react native",

    "android": "android",
    "android development": "android",

    "ios": "ios",
    "ios development": "ios",

    # =========================
    # GAME DEVELOPMENT
    # =========================

    "unity": "unity",
    "unity3d": "unity",
    "unity 3d": "unity",

    "unreal": "unreal engine",
    "unreal engine": "unreal engine",
    "unreal engine 5": "unreal engine",

    "game development": "game development",
    "game programming": "game programming",
    "gameplay programming": "gameplay programming",

    "game physics": "game physics",
    "physics": "game physics",

    "3d game development": "3d game development",
    "2d game development": "2d game development",

    "game design": "game design",

    "game ai": "game ai",
    "game artificial intelligence": "game ai",

    "blender": "blender",
    "3d modeling": "3d modeling",
    "3d modelling": "3d modeling",

    "animation": "animation",

    # =========================
    # UI / UX
    # =========================

    "ui design": "ui design",
    "ui/ux": "ui/ux",
    "ui ux": "ui/ux",

    "ux design": "ux design",
    "user experience": "ux design",

    "figma": "figma",

    "adobe xd": "adobe xd",

    # =========================
    # BLOCKCHAIN
    # =========================

    "blockchain": "blockchain",

    "solidity": "solidity",

    "smart contracts": "smart contracts",
    "smart contract": "smart contracts",

    # =========================
    # QA / TESTING
    # =========================

    "software testing": "software testing",
    "testing": "software testing",

    "test cases": "test cases",
    "test case": "test cases",

    "automation testing": "automation testing",
    "automated testing": "automation testing",

    "selenium": "selenium",

    "postman": "postman",

    # =========================
    # OTHER
    # =========================

    "oop": "oop",
    "object-oriented programming": "oop",

    "rest": "rest apis",

    "git": "git",
"github": "github",
"git hub": "github",
"authentication": "authentication",
"auth": "authentication",
"user authentication": "authentication",
"api authentication": "authentication",
"jwt authentication": "authentication",
}
def normalize_skill(skill):

    skill = str(skill).strip().lower()

    return SKILL_ALIASES.get(skill, skill)


def normalize_skills(skills):

    return {
        normalize_skill(skill)
        for skill in (skills or [])
        if str(skill).strip()
    }


# =========================================================
# PREPARE TF-IDF
# =========================================================

career_names = list(careers.keys())

career_descriptions = [
    careers[career]
    for career in career_names
]

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words=None
)

career_vectors = vectorizer.fit_transform(
    career_descriptions
)


# =========================================================
# RECOMMEND CAREER
# =========================================================

def recommend_career(
    skills,
    interests,
    favorite_subjects,
    work_style="",
    experience_level=""
):

    skills = skills or []
    interests = interests or []
    favorite_subjects = favorite_subjects or []

    skills = [str(x) for x in skills]
    interests = [str(x) for x in interests]
    favorite_subjects = [str(x) for x in favorite_subjects]

    # -----------------------------------------------------
    # Normalize student skills
    # -----------------------------------------------------

    student_skills = normalize_skills(skills)

    # -----------------------------------------------------
    # Student text
    # -----------------------------------------------------

    student_text = " ".join(
        skills +
        interests +
        favorite_subjects
    )

    # -----------------------------------------------------
    # TF-IDF
    # -----------------------------------------------------

    student_vector = vectorizer.transform(
        [student_text]
    )

    similarities = cosine_similarity(
        student_vector,
        career_vectors
    )[0]

    # =====================================================
    # CALCULATE CAREER SCORE
    # =====================================================

    career_scores = []

    for i, career in enumerate(career_names):

        # -------------------------------------------------
        # TF-IDF score
        # -------------------------------------------------

        tfidf_score = float(similarities[i])

        # -------------------------------------------------
        # Required skills
        # -------------------------------------------------

      # -------------------------------------------------
        # Required skills
        # -------------------------------------------------

        required_skills = career_requirements.get(
            career,
            []
        )

        if required_skills:

            matched_skills = [
                skill
                for skill in required_skills
                if normalize_skill(skill)
                in student_skills
            ]

            skill_coverage = (
                len(matched_skills) /
                len(required_skills)
            )

        else:

            skill_coverage = 0


        # -------------------------------------------------
        # Core skills
        # -------------------------------------------------

        core_skills = career_core_skills.get(
            career,
            []
        )

        if core_skills:

            matched_core = [
                skill
                for skill in core_skills
                if normalize_skill(skill)
                in student_skills
            ]

            core_coverage = (
                len(matched_core) /
                len(core_skills)
            )

        else:

            core_coverage = 0


        # -------------------------------------------------
        # TF-IDF
        # -------------------------------------------------

        tfidf_score = float(
            similarities[i]
        )


        # -------------------------------------------------
        # Work style
        # -------------------------------------------------

        preferred_styles = career_work_styles.get(
            career,
            []
        )

        if (
            work_style
            and work_style in preferred_styles
        ):

            work_score = 1.0

        else:

            work_score = 0.0


        # =================================================
        # FINAL CAREER SCORE
        #
        # Core Skills     = 50%
        # Required Skills = 30%
        # TF-IDF          = 15%
        # Work Style      = 5%
        # =================================================

        score = (
            core_coverage * 0.50
            +
            skill_coverage * 0.30
            +
            tfidf_score * 0.15
            +
            work_score * 0.05
        )


        career_scores.append(score)
    # =====================================================
    # SORT CAREERS
    # =====================================================

    ranked_indexes = sorted(
        range(len(career_names)),
        key=lambda i: career_scores[i],
        reverse=True
    )

    # =====================================================
    # TOP 3
    # =====================================================

    recommendations = []

    for index in ranked_indexes[:3]:

        career = career_names[index]

        recommendations.append({
            "career": career,
            "score": round(
                career_scores[index] * 100,
                2
            )
        })

    # =====================================================
    # BEST CAREER
    # =====================================================

    best_index = ranked_indexes[0]

    best_career = career_names[best_index]

    # =====================================================
    # BEST CAREER REQUIRED SKILLS
    # =====================================================

    required_skills = career_requirements.get(
        best_career,
        []
    )

    # =====================================================
    # MATCHED SKILLS
    # =====================================================

    matched_skills = [
        skill
        for skill in required_skills
        if normalize_skill(skill)
        in student_skills
    ]

    # =====================================================
    # SKILL GAPS
    # =====================================================

    skill_gaps = [
        skill
        for skill in required_skills
        if normalize_skill(skill)
        not in student_skills
    ]

    # =====================================================
    # CURRENT SKILLS
    # =====================================================

    current_skills = skills.copy()

    # =====================================================
    # OPTIONAL SKILLS
    # =====================================================

    future_skills = optional_skills.get(
        best_career,
        []
    )

    future_skills = [
        skill
        for skill in future_skills
        if normalize_skill(skill)
        not in student_skills
    ]

    # =====================================================
    # FINAL MATCH SCORE
    # =====================================================

    best_score = career_scores[best_index]

    best_score = min(
        round(best_score * 100, 2),
        100
    )

    # =====================================================
    # ROADMAP
    # =====================================================

    roadmap = roadmaps.get(
        best_career,
        []
    )

    # =====================================================
    # REASON
    # =====================================================

    if matched_skills:

        reason = (
            f"Your profile is a good match for "
            f"{best_career} because you already have "
            f"relevant skills such as "
            f"{', '.join(matched_skills[:5])}."
        )

    else:

        reason = (
            f"Your interests and profile show "
            f"potential for {best_career}."
        )

    # =====================================================
    # RETURN
    # =====================================================

    return {

        "career": best_career,

        "score": best_score,

        "reason": reason,

        "current_skills": current_skills,

        "skill_gaps": skill_gaps,

        "skills_to_learn": skill_gaps,

        "optional_skills": future_skills,

        "roadmap": roadmap,

        "top_recommendations": recommendations
    }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    result = recommend_career(

        skills=[
            "HTML",
            "CSS",
            "JavaScript",
            "GitHub"
        ],

        interests=[
            "Web Development",
            "Frontend Development"
        ],

        favorite_subjects=[
            "Programming"
        ],

        work_style="Creative",

        experience_level="Beginner"
    )

    print("\n==============================")
    print("BEST CAREER")
    print("==============================")

    print(result["career"])

    print(
        "Score:",
        result["score"],
        "%"
    )

    print("\n==============================")
    print("CURRENT SKILLS")
    print("==============================")

    for skill in result["current_skills"]:
        print("-", skill)

    print("\n==============================")
    print("SKILL GAPS")
    print("==============================")

    for skill in result["skill_gaps"]:
        print("-", skill)

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