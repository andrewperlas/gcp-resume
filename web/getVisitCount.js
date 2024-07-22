document.addEventListener('DOMContentLoaded', (event) => {
    // The URL of our Cloud Function API
    const cloudFunctionUrl = 'https://us-west1-psyched-age-416001.cloudfunctions.net/api'

    // Options for the fetch request
    const postOptions = {
        method: "GET"
    }

    // GET request
    fetch(cloudFunctionUrl, postOptions)
        .then(response => response.json())
        .then(json => p.innerHTML = json[0].description)
        .catch(error => console.error('Error:', error));
});