document.addEventListener('DOMContentLoaded', (event) => {
    // The URL of our Cloud Function API
    const cloudFunctionUrl = 'https://us-west1-psyched-age-416001.cloudfunctions.net/add-visitor-count'

    // GET request
    fetch(cloudFunctionUrl)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
});