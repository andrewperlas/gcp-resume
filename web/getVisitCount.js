document.addEventListener('DOMContentLoaded', (event) => {
    // The URL of our Cloud Function API
    const cloudFunctionUrl = 'https://resumeapi.andrewperlas.com'

    // Options for the fetch request
    const Options = {
        method: "GET"
    }

    // GET request
    fetch(cloudFunctionUrl, options)
        .then(response => response.text())
        .then(result => console.log('Success:', result))
        .catch(error => console.error('Error:', error));
});