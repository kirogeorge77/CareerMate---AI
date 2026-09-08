let currentStudentId = null;
const startBtn = document.getElementById("startBtn");
const submitBtn = document.getElementById("submitBtn");

startBtn.addEventListener("click", function () {
    document.getElementById("assessment").scrollIntoView({
        behavior: "smooth"
    });
});

submitBtn.addEventListener("click", async function (event) {

    event.stopPropagation();
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const university = document.getElementById("university").value.trim();
    const major = document.getElementById("major").value.trim();

    if (
        name === "" ||
        university === "" ||
        major === "" ||
        document.getElementById("skills").value.trim() === "" ||
        document.getElementById("interests").value.trim() === "" ||
        document.getElementById("subjects").value.trim() === ""
    ) {
        document.getElementById("message").textContent =
            "⚠️ Please fill in all fields before submitting.";

        return;
    }
    
    const year = Number(document.getElementById("year").value);

    const skills = document.getElementById("skills").value
        .split(",")
        .map(skill => skill.trim())
        .filter(skill => skill !== "");

    const interests = document.getElementById("interests").value
        .split(",")
        .map(item => item.trim())
        .filter(item => item !== "");

    const subjects = document.getElementById("subjects").value
        .split(",")
        .map(item => item.trim())
        .filter(item => item !== "");

       console.log("FORM SKILLS:", skills.join(", "));
console.log("FORM INTERESTS:", interests.join(", "));
console.log("FORM SUBJECTS:", subjects.join(", "));

    const workStyle = document.getElementById("workStyle").value;
    const experienceLevel = document.getElementById("experienceLevel").value;

    try {

        // Send student data to backend
        const studentResponse = await fetch("http://127.0.0.1:8000/students", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                university: university,
                major: major,
                year: year,
                skills: skills
            })
        });

        const studentData = await studentResponse.json();

        console.log("Student created:", studentData);
        currentStudentId = studentData.student_id;

        // Send assessment data to backend
        const assessmentResponse = await fetch("http://127.0.0.1:8000/assessment", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                student_id: studentData.student_id,
                interests: interests,
                favorite_subjects: subjects,
                work_style: workStyle,
                experience_level: experienceLevel
            })
        });

        const assessmentData = await assessmentResponse.json();

        console.log("Assessment created:", assessmentData);

        document.getElementById("message").textContent =
            "✅ Assessment submitted successfully!";
            const recommendationResponse = await fetch(
    "http://127.0.0.1:8000/recommend",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            student_id: studentData.student_id,
        })
    }
);

const recommendation = await recommendationResponse.json();
console.log("AI Recommendation:", recommendation);

document.getElementById("result").innerHTML = `
    <h2>🎯 Your Career Recommendation</h2>

    <h3>${recommendation.recommended_career}</h3>

    <p><strong>Match Score:</strong> ${recommendation.match_score}%</p>

    <p><strong>Why?</strong> ${recommendation.reason}</p>

    <h4>📚 Skills to Learn</h4>
    <ul>
        ${recommendation.skills_to_learn.map(skill => `<li>${skill}</li>`).join("")}
    </ul>

    <h4>🗺️ Your Roadmap</h4>
    <ol>
        ${recommendation.roadmap.map(step => `<li>${step}</li>`).join("")}
    </ol>
`;
            

    } catch (error) {

        console.error(error);

        document.getElementById("message").textContent =
            "❌ Something went wrong. Make sure the backend is running.";
    }
});
const askBtn = document.getElementById("askBtn");

askBtn.addEventListener("click", async function () {

    const question = document.getElementById("assistantQuestion").value;
    if (question.trim() === "") {
    document.getElementById("assistantAnswer").textContent =
        "⚠️ Please enter a question first.";

    return;
}
if (currentStudentId === null) {
    document.getElementById("assistantAnswer").textContent =
        "⚠️ Please complete the Career Assessment first.";

    return;
}

    const response = await fetch(
        "http://127.0.0.1:8000/career-assistant",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                student_id: currentStudentId,
                question: question
            })
        }
    );

    const data = await response.json();

    document.getElementById("assistantAnswer").textContent =
        data.answer;
});