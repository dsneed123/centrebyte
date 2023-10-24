document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const searchButton = document.getElementById("search-button");

    searchButton.addEventListener("click", function () {
        const searchQuery = searchInput.value;
        if (searchQuery.trim() !== "") {
            // Redirect to the Django search view with the search query as a parameter
            window.location.href = `/search/?q=${searchQuery}`;
        }
    });
});
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
    window.location.href = '/register-item/'; // Replace with the actual URL of your "Sell an Item" page
});
const accountBtn = document.getElementById('account-btn');

// Add a click event listener to the button
    accountBtn.addEventListener('click', function () {
    // Redirect to the "Sell an Item" page
    window.location.href = '/accounts/profile'; // Replace with the actual URL of your "Sell an Item" page
});
const cartBtn = document.getElementById('last-element');

// Add a click event listener to the button
    cartBtn.addEventListener('click', function () {
    // Redirect to the "Sell an Item" page
    window.location.href = '/cart/'; // Replace with the actual URL of your "Sell an Item" page
});
const logoutLink = document.getElementById('logout-link');
const logoutNotification = document.getElementById('logout-notification');

logoutLink.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent the default link behavior (navigating to the logout URL)
    logoutNotification.style.display = 'block';
    setTimeout(() => {
        logoutNotification.style.display = 'none';
    }, 3000); // Hide the notification after 3 seconds (adjust as needed)
    window.location.href = '/logout/';
});



