let currentStudentId = null;

const startBtn = document.getElementById("startBtn");
const submitBtn = document.getElementById("submitBtn");
const cvFile = document.getElementById("cvFile");
const chooseFileBtn = document.getElementById("chooseFileBtn");
const uploadBox = document.getElementById("uploadBox");
const fileName = document.getElementById("fileName");


// =========================================================
// START BUTTON
// =========================================================

startBtn.addEventListener("click", function () {

    document.getElementById("assessment").scrollIntoView({
        behavior: "smooth"
    });

});


// =========================================================
// CHOOSE FILE
// =========================================================

chooseFileBtn.addEventListener("click", function (event) {

    event.stopPropagation();

    cvFile.click();

});


// =========================================================
// CLICK UPLOAD BOX
// =========================================================

uploadBox.addEventListener("click", function () {

    cvFile.click();

});


// =========================================================
// FILE SELECTED
// =========================================================

cvFile.addEventListener("change", function () {

    if (cvFile.files.length > 0) {

        fileName.textContent =
            "Selected File: " + cvFile.files[0].name;

    }

});


// =========================================================
// DRAG AND DROP
// =========================================================

uploadBox.addEventListener("dragover", function (event) {

    event.preventDefault();

    uploadBox.classList.add("dragging");

});


uploadBox.addEventListener("dragleave", function () {

    uploadBox.classList.remove("dragging");

});


uploadBox.addEventListener("drop", function (event) {

    event.preventDefault();

    uploadBox.classList.remove("dragging");

    const file = event.dataTransfer.files[0];

    if (file) {

        cvFile.files = event.dataTransfer.files;

        fileName.textContent =
            "Selected File: " + file.name;

    }

});


// =========================================================
// ANALYZE CV
// =========================================================

submitBtn.addEventListener("click", async function (event) {

    event.preventDefault();

    const messageBox =
        document.getElementById("message");

    const resultBox =
        document.getElementById("result");


    // -----------------------------------------------------
    // Check file
    // -----------------------------------------------------

    if (cvFile.files.length === 0) {

        messageBox.textContent =
            "⚠️ Please upload your CV first.";

        return;
    }


    const file = cvFile.files[0];


    // -----------------------------------------------------
    // Check file size
    // -----------------------------------------------------

    if (file.size > 10 * 1024 * 1024) {

        messageBox.textContent =
            "⚠️ File size must be less than 10MB.";

        return;
    }


    // -----------------------------------------------------
    // Check extension
    // -----------------------------------------------------

    const fileNameLower =
        file.name.toLowerCase();

    const isAllowed =
        fileNameLower.endsWith(".pdf") ||
        fileNameLower.endsWith(".docx") ||
        fileNameLower.endsWith(".txt");


    if (!isAllowed) {

        messageBox.textContent =
            "⚠️ Please upload a PDF, DOCX, or TXT file.";

        return;
    }


    // -----------------------------------------------------
    // Start loading
    // -----------------------------------------------------

    try {

        messageBox.textContent =
            "⏳ Uploading and analyzing your CV...";

        resultBox.innerHTML = "";


        // -------------------------------------------------
        // Create FormData
        // -------------------------------------------------

        const formData =
            new FormData();

        formData.append(
            "file",
            file
        );


        // -------------------------------------------------
        // Send CV
        // -------------------------------------------------

        const response =
            await fetch(
                "http://127.0.0.1:8000/analyze-cv",
                {
                    method: "POST",
                    body: formData
                }
            );


        // -------------------------------------------------
        // Backend error
        // -------------------------------------------------

        if (!response.ok) {

            let errorMessage =
                "Something went wrong.";

            try {

                const errorData =
                    await response.json();

                if (errorData.detail) {

                    errorMessage =
                        errorData.detail;

                }

            } catch (error) {

                console.log(
                    "Could not read backend error."
                );

            }

            throw new Error(
                errorMessage
            );
        }


        // -------------------------------------------------
        // Get JSON
        // -------------------------------------------------

        const data =
            await response.json();


        console.log(
            "CV Analysis:",
            data
        );


        // -------------------------------------------------
        // IMPORTANT:
        // Save REAL student ID
        // -------------------------------------------------

        if (!data.student_id) {

            throw new Error(
                "Backend did not return a student ID."
            );

        }

        currentStudentId =
            data.student_id;


        // -------------------------------------------------
        // Success
        // -------------------------------------------------

        messageBox.textContent =
            "✅ CV analyzed successfully!";


        // -------------------------------------------------
        // Render result
        // -------------------------------------------------

        renderCareerResult(
            data
        );


        // -------------------------------------------------
        // Scroll to result
        // -------------------------------------------------

        setTimeout(function () {

            resultBox.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        }, 200);


    } catch (error) {

        console.error(
            "CV Analysis Error:",
            error
        );


        messageBox.textContent =
            "❌ CV analysis failed.";


        resultBox.innerHTML = `
            <div class="error-box">
                <strong>Error:</strong>
                ${escapeHTML(error.message)}
            </div>
        `;

    }

});


// =========================================================
// RENDER CAREER RESULT
// =========================================================

function renderCareerResult(data) {

    const resultBox =
        document.getElementById("result");


    // -----------------------------------------------------
    // Current Skills
    // -----------------------------------------------------

    const currentSkills =
        data.current_skills || [];


    // -----------------------------------------------------
    // Skill Gaps
    // -----------------------------------------------------

    const skillGaps =
        data.skill_gaps ||
        data.skills_to_learn ||
        [];


    // -----------------------------------------------------
    // Optional Skills
    // -----------------------------------------------------

    const optionalSkills =
        data.optional_skills || [];


    // -----------------------------------------------------
    // Roadmap
    // -----------------------------------------------------

    const roadmap =
        data.roadmap || [];


    // -----------------------------------------------------
    // Top Careers
    // -----------------------------------------------------

    const topRecommendations =
        data.top_recommendations || [];


    // -----------------------------------------------------
    // Build Current Skills HTML
    // -----------------------------------------------------

    let currentSkillsHTML = "";

    if (currentSkills.length > 0) {

        currentSkillsHTML = currentSkills
            .map(function (skill) {

                return `
                    <li>
                        <span class="skill-check">✓</span>
                        ${escapeHTML(skill)}
                    </li>
                `;

            })
            .join("");

    } else {

        currentSkillsHTML = `
            <li>No skills detected.</li>
        `;

    }


    // -----------------------------------------------------
    // Build Skill Gaps HTML
    // -----------------------------------------------------

    let skillGapsHTML = "";

    if (skillGaps.length > 0) {

        skillGapsHTML = skillGaps
            .map(function (skill) {

                return `
                    <li>
                        <span class="skill-gap">!</span>
                        ${escapeHTML(skill)}
                    </li>
                `;

            })
            .join("");

    } else {

        skillGapsHTML = `
            <li>
                Great! No major skill gaps detected.
            </li>
        `;

    }


    // -----------------------------------------------------
    // Build Optional Skills HTML
    // -----------------------------------------------------

    let optionalSkillsHTML = "";

    if (optionalSkills.length > 0) {

        optionalSkillsHTML = optionalSkills
            .map(function (skill) {

                return `
                    <li>
                        <span class="optional-skill">+</span>
                        ${escapeHTML(skill)}
                    </li>
                `;

            })
            .join("");

    } else {

        optionalSkillsHTML = `
            <li>No optional skills available.</li>
        `;

    }


    // -----------------------------------------------------
    // Build Roadmap HTML
    // -----------------------------------------------------

    let roadmapHTML = "";

    if (roadmap.length > 0) {

        roadmapHTML = roadmap
            .map(function (step, index) {

                return `
                    <li>
                        <span class="roadmap-number">
                            ${index + 1}
                        </span>

                        <span>
                            ${escapeHTML(step)}
                        </span>
                    </li>
                `;

            })
            .join("");

    } else {

        roadmapHTML = `
            <li>
                Roadmap is not available.
            </li>
        `;

    }


    // -----------------------------------------------------
    // Build Top Recommendations
    // -----------------------------------------------------

    let topCareersHTML = "";

    if (topRecommendations.length > 0) {

        topCareersHTML = topRecommendations
            .map(function (item, index) {

                return `
                    <div class="career-option">

                        <span>
                            ${index + 1}.
                            ${escapeHTML(item.career)}
                        </span>

                        <strong>
                            ${item.score ?? 0}%
                        </strong>

                    </div>
                `;

            })
            .join("");

    }


    // -----------------------------------------------------
    // Final Result
    // -----------------------------------------------------

    resultBox.innerHTML = `

        <div class="career-result">

            <!-- =========================================
                 CAREER
            ========================================== -->

            <div class="result-section main-career">

                <div class="section-icon">
                    🎯
                </div>

                <div>

                    <h2>
                        Your Career Recommendation
                    </h2>

                    <h3>
                        ${escapeHTML(
                            data.recommended_career ||
                            "Not available"
                        )}
                    </h3>

                </div>

            </div>


            <!-- =========================================
                 SCORE
            ========================================== -->

            <div class="score-card">

                <div>

                    <span>
                        Match Score
                    </span>

                    <strong>
                        ${data.match_score ?? "N/A"}%
                    </strong>

                </div>

                <div class="score-bar">

                    <div
                        class="score-progress"
                        style="
                            width: ${Math.min(
                                Number(data.match_score) || 0,
                                100
                            )}%;
                        "
                    ></div>

                </div>

            </div>


            <!-- =========================================
                 WHY
            ========================================== -->

            <div class="result-section">

                <h4>
                    💡 Why this career?
                </h4>

                <p>
                    ${escapeHTML(
                        data.reason ||
                        "No reason provided."
                    )}
                </p>

            </div>


            <!-- =========================================
                 CURRENT SKILLS
            ========================================== -->

            <div class="result-section">

                <h4>
                    ✅ Your Current Skills
                </h4>

                <ul class="skills-list">
                    ${currentSkillsHTML}
                </ul>

            </div>


            <!-- =========================================
                 SKILL GAPS
            ========================================== -->

            <div class="result-section">

                <h4>
                    📚 Skills You Should Learn
                </h4>

                <p class="section-description">
                    These skills can help you become
                    stronger in your recommended career.
                </p>

                <ul class="skills-list">
                    ${skillGapsHTML}
                </ul>

            </div>


            <!-- =========================================
                 OPTIONAL SKILLS
            ========================================== -->

            <div class="result-section">

                <h4>
                    💡 Optional Future Skills
                </h4>

                <p class="section-description">
                    These are not required now,
                    but can help you grow later.
                </p>

                <ul class="skills-list">
                    ${optionalSkillsHTML}
                </ul>

            </div>


            <!-- =========================================
                 ROADMAP
            ========================================== -->

            <div class="result-section">

                <h4>
                    🗺️ Your Personalized Roadmap
                </h4>

                <ol class="roadmap-list">
                    ${roadmapHTML}
                </ol>

            </div>


            <!-- =========================================
                 TOP 3
            ========================================== -->

            ${
                topCareersHTML
                    ? `
                        <div class="result-section">

                            <h4>
                                🏆 Other Career Matches
                            </h4>

                            <div class="career-options">
                                ${topCareersHTML}
                            </div>

                        </div>
                    `
                    : ""
            }

        </div>

    `;

}


// =========================================================
// CAREER ASSISTANT
// =========================================================

const askBtn =
    document.getElementById("askBtn");


askBtn.addEventListener(
    "click",
    async function () {

        const question =
            document
                .getElementById(
                    "assistantQuestion"
                )
                .value
                .trim();


        const answerBox =
            document.getElementById(
                "assistantAnswer"
            );


        // -------------------------------------------------
        // Check question
        // -------------------------------------------------

        if (question === "") {

            answerBox.textContent =
                "⚠️ Please enter a question first.";

            return;
        }


        // -------------------------------------------------
        // Check CV
        // -------------------------------------------------

        if (currentStudentId === null) {

            answerBox.textContent =
                "⚠️ Please analyze your CV first.";

            return;
        }


        try {

            answerBox.textContent =
                "⏳ Career Assistant is thinking...";


            const response =
                await fetch(
                    "http://127.0.0.1:8000/career-assistant",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            student_id:
                                currentStudentId,

                            question:
                                question

                        })
                    }
                );


            // -------------------------------------------------
            // Backend error
            // -------------------------------------------------

            if (!response.ok) {

                let errorMessage =
                    "Something went wrong.";

                try {

                    const errorData =
                        await response.json();

                    if (errorData.detail) {

                        errorMessage =
                            errorData.detail;

                    }

                } catch (error) {

                    console.log(
                        "Could not read assistant error."
                    );

                }

                throw new Error(
                    errorMessage
                );
            }


            // -------------------------------------------------
            // Get answer
            // -------------------------------------------------

            const data =
                await response.json();


            if (data.answer) {

                answerBox.innerHTML =
                    formatAssistantAnswer(
                        data.answer
                    );

            } else {

                answerBox.textContent =
                    "❌ No answer received from Career Assistant.";

            }


        } catch (error) {

            console.error(
                "Career Assistant Error:",
                error
            );

            answerBox.textContent =
                "❌ " + error.message;

        }

    }
);


// =========================================================
// FORMAT ASSISTANT ANSWER
// =========================================================

function formatAssistantAnswer(
    text
) {

    if (!text) {
        return "";
    }


    let safeText =
        escapeHTML(text);


    // Bold markdown
    safeText =
        safeText.replace(
            /\*\*(.*?)\*\*/g,
            "<strong>$1</strong>"
        );


    // New lines
    safeText =
        safeText.replace(
            /\n/g,
            "<br>"
        );


    return safeText;

}


// =========================================================
// ESCAPE HTML
// Prevent AI output from injecting HTML
// =========================================================

function escapeHTML(value) {

    if (value === null || value === undefined) {

        return "";

    }

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}