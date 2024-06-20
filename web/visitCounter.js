// Check if localStorage is available
if (typeof (Storage) !== "undefined") {
    // Retrieve the current visit count
    let visitCount = localStorage.getItem('visitCount');

    // If visitCount is not available, initialize it to 0
    if (visitCount === null) {
        visitCount = 0;
    }

    // Increment the visit count
    visitCount++;

    // Store the updated visit count back in localStorage
    localStorage.setItem('visitCount', visitCount);

    // Display the visit count in the HTML element
    document.getElementById('visit-count').innerText = visitCount;
} else {
    // If localStorage is not supported, display a message
    document.getElementById('visit-count').innerText = "localStorage is not supported by your browser.";
}