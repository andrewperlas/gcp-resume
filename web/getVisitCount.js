document.addEventListener('DOMContentLoaded', (event) => {
    // The URL of our Cloud Function API
    const cloudFunctionUrl = 'https://resumeapi.andrewperlas.com'

    // Options for the fetch request
    const Options = {
        method: "GET"
    }

    // GET request
    fetch(cloudFunctionUrl, Options)
        .then(response => response.json())
        .then(json => p.innerHTML = json[0].id)
        .catch(error => console.error('Error:', error));
});