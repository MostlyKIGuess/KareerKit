// Get DOM elements
const usernameInput = document.getElementById('twitterUsername');
const processButton = document.getElementById('processButton');
const resultMessage = document.getElementById('resultMessage');
const loadingMessage = document.getElementById('loadingMessage'); // Add this line
const messageText = document.getElementById('messageText');

// Add event listener to the Process button
processButton.addEventListener('click', () => {
    const twitterUsername = usernameInput.value;

    // Show loading message while waiting for the Python script response
    resultMessage.classList.add('hidden');
    loadingMessage.classList.remove('hidden');

    // Make an AJAX request to your Python script
    fetch('/process_username', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: twitterUsername }),
    })
        .then(response => response.json())
        .then(data => {
            loadingMessage.classList.add('hidden');
            resultMessage.classList.remove('hidden');
            messageText.innerText = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
