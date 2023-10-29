function getJobRecommendations() {
    const mbtiType = document.getElementById("mbti").value;
    const enneagramType = document.getElementById("enneagram").value;
    
    // Make an API call to the ChatGPT API to get job recommendations based on the personality types.
    // Replace 'YOUR_API_KEY' with your actual API key.
    const apiKey = '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';

    fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            model: 'gpt-3.5-turbo',
            messages: [
                { role: 'system', content: 'You are a helpful assistant that provides job recommendations.' },
                { role: 'user', content: `My MBTI type is ${mbtiType} and my Enneagram type is ${enneagramType}.` },
                { role: 'assistant', content: 'What jobs do you recommend for me?' },
            ],
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Extract and display the job recommendations from the API response.
        const jobList = document.getElementById("job-list");
        jobList.innerHTML = ""; // Clear previous results

        const recommendations = data.choices[0].message.content.split('\n');
        recommendations.forEach((job, index) => {
            const listItem = document.createElement("li");
            listItem.textContent = job;
            jobList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));
}
