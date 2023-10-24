const profileBtn = document.getElementById('my-profile');

// Add a click event listener to the button
    profileBtn.addEventListener('click', function () {
    // Redirect to the "Sell an Item" page
    window.location.href = '/accounts/profile/'; // Replace with the actual URL of your "Sell an Item" page
});
const manageItemsBtn = document.getElementById('manage-items');

// Add a click event listener to the button
    manageItemsBtn.addEventListener('click', function () {
        console.log('click');
    // Redirect to the "Sell an Item" page
    window.location.href = '/accounts/profile/user_items/'; // Replace with the actual URL of your "Sell an Item" page
});