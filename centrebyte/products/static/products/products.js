// Add this script to your HTML or include it from an external JS file
document.addEventListener("DOMContentLoaded", function() {
    const readMoreButtons = document.querySelectorAll(".read-more");

    readMoreButtons.forEach(button => {
        button.addEventListener("click", function() {
            // Retrieve the item ID from the data attribute
            const itemId = button.getAttribute("data-item-id");

            // Redirect to the desired URL with the item ID
            window.location.href = `/product/${itemId}`;
        });
    });
});

