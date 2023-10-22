from django.http import JsonResponse
from django.views.decorators.http import require_POST
from bitcoinlib.wallets import Wallet, wallet_delete
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Cart
import qrcode
from PIL import Image
from io import BytesIO
import base64

@login_required
def crypto_payment(request):
    """
    Display the total price and generate a QR code to display.
    """
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.price for cart in cart_items for item in cart.items.all())

    # Create the wallet name
    wallet_name = request.user.username

    try:
        # Attempt to load the wallet, which will raise an exception if it doesn't exist
        existing_wallet = Wallet(wallet_name)
        print(f"wallet {wallet_name} already exists. Deleting and creating a new one")
    except Exception:
        print(f"wallet {wallet_name} does not exist")
        existing_wallet = None

    # Check if the wallet already exists; if it does, delete it and recreate
    if existing_wallet is not None:
        wallet_delete(wallet_name)

    # Create the wallet
    Wallet.create(wallet_name)

    # Generate a QR code for a unique identifier (e.g., user's username)
    key1 = Wallet(wallet_name).get_key()
    unique_identifier = key1.address

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(unique_identifier)
    qr.make(fit=True)

    # Create a QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a BytesIO object
    image_stream = BytesIO()
    img.save(image_stream, format="PNG")
    image_stream.seek(0)

    # Convert the image stream to a base64-encoded string
    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    image_stream.seek(0)
    
    balance = Wallet(wallet_name).balance()
    print(f"Balance for wallet '{wallet_name}': {balance:.8f} BTC")
    

    # Include wallet_name in the context
    context = {
        'total_price': total_price,
        'qr_image_base64': image_base64,
        'wallet_name': wallet_name,  # Include the wallet name in the context
        'wallet_address':key1.address,
        'balance': f'{balance:.8f}',
    }

    return render(request, 'payment.html', context)

@require_POST
def delete_wallet(request):
    # Implement security checks, e.g., user authentication and CSRF protection
    wallet_name = request.POST.get('wallet_name')

    try:
        wallet_delete(wallet_name)
        print("successfully deleted wallet")
        return JsonResponse({'message': 'Wallet deleted successfully'})
    except Exception as e:
        print("failed to delete wallet")
        return JsonResponse({'message': f'Failed to delete wallet: {str(e)}'}, status=500)
