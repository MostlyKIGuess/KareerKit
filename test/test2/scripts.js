// In the original quiz page

const showResultButton = document.getElementById("show-result-button");
showResultButton.addEventListener("click", () => {
    const resultWindow = window.open("result.html", "_blank");

    // Calculate personality scores and determine main personality and wing
    const personalityScores = [
        personality1Score, personality2Score, personality3Score, personality4Score,
        personality5Score, personality6Score, personality7Score, personality8Score, personality9Score
    ];

    const personalities = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];

    const maxScore = Math.max(...personalityScores);
    const mainPersonality = personalities[personalityScores.indexOf(maxScore)];
    let wing;

    if (mainPersonality === "1") {
        // Determine the wing for Personality 1
        const wingScores = [personality2Score, personality9Score];
        const maxWingScore = Math.max(...wingScores);
        wing = maxWingScore > 0 ? personalities[wingScores.indexOf(maxWingScore)] : "1";
    } else if (mainPersonality === "2") {
        // Determine the wing for Personality 2
        const wingScores = [personality1Score, personality3Score];
        const maxWingScore = Math.max(...wingScores);
        wing = maxWingScore > 0 ? personalities[wingScores.indexOf(maxWingScore)] : "2";
    }
    // Add more conditions for other main personalities (3-9) here

    // Display the results on the result page
    resultWindow.onload = function() {
        const resultDocument = resultWindow.document;

        const table = resultDocument.querySelector("table");
        const mainPersonalityText = resultDocument.getElementById("main-personality");

        // Fill in the table rows with personality scores
        for (let i = 0; i < personalities.length; i++) {
            const row = table.insertRow(i + 1);
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);
            cell1.innerHTML = `Personality ${personalities[i]}`;
            cell2.innerHTML = personalityScores[i];
        }

        // Display the main personality and its wing
        mainPersonalityText.textContent = `Your main personality is ${mainPersonality}w${wing}`;
    };
});
