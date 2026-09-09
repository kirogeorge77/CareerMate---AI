
let currentStudentId = null;

const startBtn = document.getElementById("startBtn");
const submitBtn = document.getElementById("submitBtn");
const cvFile = document.getElementById("cvFile");
const chooseFileBtn = document.getElementById("chooseFileBtn");
const uploadBox = document.getElementById("uploadBox");
const fileName = document.getElementById("fileName");

// =========================
// START BUTTON
// =========================

startBtn.addEventListener("click", function () {
    document.getElementById("assessment").scrollIntoView({
        behavior: "smooth"
    });
});

// =========================
// CHOOSE FILE
// =========================

chooseFileBtn.addEventListener("click", function (event) {
    event.stopPropagation();
    cvFile.click();
});

// =========================
// CLICK UPLOAD BOX
// =========================

uploadBox.addEventListener("click", function () {
    cvFile.click();
});

// =========================
// FILE SELECTED
// =========================

cvFile.addEventListener("change", function () {
    if (cvFile.files.length > 0) {
        fileName.textContent =
            "Selected File: " + cvFile.files[0].name;
    }
});

// =========================
// DRAG AND DROP
// =========================

uploadBox.addEventListener("dragover", function (event) {
    event.preventDefault();
});

uploadBox.addEventListener("drop", function (event) {
    event.preventDefault();

    const file = event.dataTransfer.files[0];

    if (file) {
        cvFile.files = event.dataTransfer.files;

        fileName.textContent =
            "Selected File: " + file.name;
    }
});

// =========================
// ANALYZE CV
// =========================

submitBtn.addEventListener("click", async function (event) {
    event.preventDefault();

    const messageBox = document.getElementById("message");
    const resultBox = document.getElementById("result");

    // Check if file exists
    if (cvFile.files.length === 0) {
        messageBox.textContent =
            "⚠️ Please upload your CV first.";
        return;
    }

    const file = cvFile.files[0];

    // Check file size (10 MB)
    if (file.size > 10 * 1024 * 1024) {
        messageBox.textContent =
            "⚠️ File size must be less than 10MB.";
        return;
    }

    // Check file type
    const allowedExtensions = [
        "application/pdf",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ];

    if (!allowedExtensions.includes(file.type)) {
        messageBox.textContent =
            "⚠️ Please upload a PDF, DOC, or DOCX file.";
        return;
    }

    try {
        messageBox.textContent =
            "⏳ Uploading and analyzing your CV...";

        resultBox.innerHTML = "";

        // Create FormData
        const formData = new FormData();
        formData.append("file", file);

        // Send CV to Backend
        const response = await fetch(
            "http://127.0.0.1:8000/analyze-cv",
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(
                `Backend error: ${response.status} - ${errorText}`
            );
        }

        const data = await response.json();

        console.log("CV Analysis:", data);

        // Save student ID if backend returns one
        if (data.student_id) {
            currentStudentId = data.student_id;
        }

        messageBox.textContent =
            "✅ CV analyzed successfully!";

        // Display Recommendation
        resultBox.innerHTML = `
            <h2>🎯 Your Career Recommendation</h2>

            <h3>${data.recommended_career || "Not available"}</h3>

            <p>
                <strong>Match Score:</strong>
                ${data.match_score ?? "N/A"}%
            </p>

            <p>
                <strong>Why?</strong>
                ${data.reason || "No reason provided."}
            </p>

            <h4>📚 Skills to Learn</h4>

            <ul>
                ${(data.skills_to_learn || [])
                    .map(skill => `<li>${skill}</li>`)
                    .join("")}
            </ul>

            <h4>🗺️ Your Roadmap</h4>

            <ol>
                ${(data.roadmap || [])
                    .map(step => `<li>${step}</li>`)
                    .join("")}
            </ol>
        `;

    } catch (error) {
        console.error("CV Analysis Error:", error);

        messageBox.textContent =
            "❌ Something went wrong. Make sure the backend is running.";

        resultBox.innerHTML = `
            <p>
                <strong>Error:</strong> ${error.message}
            </p>
        `;
    }
});

// =========================
// CAREER ASSISTANT
// =========================

const askBtn = document.getElementById("askBtn");

askBtn.addEventListener("click", async function () {
    const question = document
        .getElementById("assistantQuestion")
        .value
        .trim();

    const answerBox =
        document.getElementById("assistantAnswer");

    if (question === "") {
        answerBox.textContent =
            "⚠️ Please enter a question first.";
        return;
    }

    if (currentStudentId === null) {
        answerBox.textContent =
            "⚠️ Please analyze your CV first.";
        return;
    }

    try {
        answerBox.textContent =
            "⏳ Career Assistant is thinking...";

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

        if (!response.ok) {
            const errorText = await response.text();

            throw new Error(
                `Backend error: ${response.status} - ${errorText}`
            );
        }

        const data = await response.json();

        if (data.answer) {
            answerBox.innerHTML = data.answer
                .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
                .replace(/\n/g, "<br>");
        } else {
            answerBox.textContent =
                "❌ No answer received from Career Assistant.";
        }

    } catch (error) {
        console.error("Career Assistant Error:", error);

        answerBox.textContent =
            "❌ Something went wrong. Make sure the backend is running.";
    }
});

