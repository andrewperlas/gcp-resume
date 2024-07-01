document.addEventListener('DOMContentLoaded', (event) => {
    // The URL of our Cloud Function API
    const cloudFunctionUrl = 'https://us-west1-psyched-age-416001.cloudfunctions.net/add-visitor-count'

    // Data to send in a POST request
    const data = {
        message: 'Knock knock from the resume website!'
    };

    // Get current visit count
    const getOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    };

    // GET request
    fetch(cloudFunctionUrl, getOptions)
        .then(response => response.json())
        .then(result => console.log(result))
        .catch(error => console.error('Error:', error));
});