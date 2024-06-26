document.addEventListener('DOMContentLoaded', (event) => {
    // The URL of our Cloud Function API
    const cloudFunctionUrl = 'https://us-west1-psyched-age-416001.cloudfunctions.net/add-visitor-count'

    // Data to send in a POST request
    const data = {
        message: 'Knock knock from the resume website!'
    };

    // Options for the fetch request
    const postOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    // Send the POST request
    fetch(cloudFunctionUrl, postOptions)
        .then(response => response.text())
        .then(result => console.log('Success:', result))
        .catch(error => console.error('Error:', error));
});