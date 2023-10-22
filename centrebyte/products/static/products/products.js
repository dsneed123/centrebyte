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
function showPrice(element) {
    element.textContent = "{{ item.price }}";
  }

  function addItemToCart() {
    // Your code to add the item to the cart
    
    // Show the notification
    $('#cart-notification').show();

    // Hide the notification after a delay (e.g., 3 seconds)
    setTimeout(function () {
        $('#cart-notification').hide();
    }, 3000);
}
function editItem(itemId) {
    var editForm = document.getElementById('edit-form-' + itemId);
    editForm.style.display = 'block';
}

function cancelEdit(itemId) {
    var editForm = document.getElementById('edit-form-' + itemId);
    editForm.style.display = 'none';
}