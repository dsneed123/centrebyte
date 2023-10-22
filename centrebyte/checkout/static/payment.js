// This function sends a POST request to delete the wallet
function deleteWallet() {
    var csrftoken = getCookie('csrftoken'); // Replace with your method to get the CSRF token
    var walletName = document.querySelector('input[name="wallet_name"]').value;

    var deleteWalletUrl = '/payment/delete_wallet/'; // Define the URL path manually

    fetch(deleteWalletUrl, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'wallet_name=' + walletName,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


// Add an event listener for the beforeunload event
window.addEventListener('beforeunload', function (event) {
    // Prevent the event from firing multiple times
    event.preventDefault();

    // Delete the wallet
    deleteWallet();
});

// Function to get the CSRF token from cookies
function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}
