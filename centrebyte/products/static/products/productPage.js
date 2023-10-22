document.addEventListener("DOMContentLoaded", function() {
    const backButton = document.getElementById("backButton");

    backButton.addEventListener("click", function() {
        window.location.href = "/";
    });
});
$(document).ready(function() {
    $(".add-to-cart").on("click", function() {
        var itemId = $(this).data("item-id");
        $.ajax({
            url: '/add_to_cart/' + itemId + '/',
            method: 'GET',
            success: function(data) {
                // Handle success (e.g., show a confirmation message)
                console.log("Item added to cart.");
            },
            error: function(error) {
                // Handle errors
                console.error("Error adding item to cart.");
            }
        });
    });
});
