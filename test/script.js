const form = document.getElementById("quiz-form");
const resultContainer = document.getElementById("result-container");
const nextButton = document.getElementById("next-button");
const questionText = document.getElementById("question-text");
const optionsContainer = document.getElementById("options-container");

let currentQuestionIndex = 0;

// Initialize accumulatedScores array to keep track of personality trait scores
const accumulatedScores = Array(9).fill(0);

function showNextQuestion() {
    if (currentQuestionIndex < quizData.length) {
        const questionData = quizData[currentQuestionIndex];
        questionText.textContent = questionData.question;
    } else {
        displayResult();
    }
}

// Function to update the accumulated scores after each question
function updateAccumulatedScores(score) {
    for (let i = 0; i < accumulatedScores.length; i++) {
        accumulatedScores[i] += quizData[currentQuestionIndex].options[i] * score;
    }
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const selectedOption = document.querySelector('input[name="q"]:checked');
    if (selectedOption) {
        const score = parseFloat(selectedOption.value);
        updateAccumulatedScores(score); // Update the accumulated scores based on user's response
    }
    currentQuestionIndex++;
    showNextQuestion();
    if (currentQuestionIndex === quizData.length) {
        displayResult(); // Display result after the last question
    }
});
