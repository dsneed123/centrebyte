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
// products.js
document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.edit-button');

    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const targetId = button.getAttribute('data-target-id');
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.style.display = 'block';
            }
        });
    });
});

