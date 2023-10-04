document.addEventListener('DOMContentLoaded', function() {
    const returnButton = document.getElementById('first-element');
    var indexUrl = '/'; // Change this to the desired URL
    // Remove the print("click") statement
    returnButton.addEventListener('click', function() {
        // Navigate to the index URL when the button is clicked
        window.location.href = indexUrl;
    });
});
const sellItemButton = document.getElementById('sell-item-button');

// Add a click event listener to the button
sellItemButton.addEventListener('click', function () {
    // Redirect to the "Sell an Item" page
    window.location.href = '/register-seller/'; // Replace with the actual URL of your "Sell an Item" page
});