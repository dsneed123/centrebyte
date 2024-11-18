# CentreByte - Bitcoin Marketplace (Proof of Concept)

CentreByte is a decentralized marketplace designed to facilitate peer-to-peer (P2P) transactions using Bitcoin as the primary currency. It provides a platform for users to buy and sell goods and services directly, similar to eBay, but with the added benefit of cryptocurrency for secure, fast, and low-fee transactions.

This project serves as a **Proof of Concept** to demonstrate the feasibility of using Bitcoin in a decentralized e-commerce environment. It showcases the potential of blockchain-based systems in facilitating global trade while maintaining user privacy and security.

## Features

- **Peer-to-Peer Transactions**: Buyers and sellers interact directly, with no middleman.
- **Bitcoin Payments**: All transactions are settled in Bitcoin, offering benefits like lower fees, faster payments, and global accessibility.
- **Listing Creation**: Sellers can list products or services with detailed descriptions, prices in Bitcoin, and shipping options.
- **Search & Filters**: Users can easily search for products, apply filters, and browse listings by category, price range, and seller reputation.
- **Escrow System**: To enhance trust, CentreByte includes an escrow mechanism that holds payments until both parties confirm the transaction, ensuring fairness and security.
- **User Reputation**: Sellers and buyers can leave feedback and ratings, building trust within the community.

## Purpose

CentreByte is designed as a **Proof of Concept** to explore the practical use of Bitcoin in a decentralized marketplace environment. The goal is to:
- Demonstrate the viability of using cryptocurrency for e-commerce.
- Promote decentralization and financial inclusion by leveraging blockchain technology.
- Provide a user-friendly interface to facilitate easy adoption of Bitcoin-based transactions.

## Tech Stack

CentreByte is built using the following technologies:

- **Backend**: Django (Python web framework)
- **Database**: SQLite (for easy setup and development)
- **Frontend**: HTML, CSS, JavaScript (with React.js for dynamic content and interactivity)
- **Bitcoin Integration**: Bitcoin payment processing is integrated using available APIs for transaction management.
- **Escrow Mechanism**: Built-in smart contract-like logic (handled server-side in Django) to manage payment releases.
  
## Setup & Installation

To get started with CentreByte locally, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/centrebyte.git
cd centrebyte
```

### 2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up the database:

CentreByte uses SQLite by default, so no external database setup is required. Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 5. Create a superuser (for admin access):

```bash
python manage.py createsuperuser
```

### 6. Run the development server:

```bash
python manage.py runserver
```

Once the server is running, you can access the site at `http://127.0.0.1:8000`.

## Usage

- **Browse Listings**: Navigate through the homepage and browse various categories to find products.
- **Create Listings**: Sellers can create product listings by logging in and using the "Create Listing" page.
- **Make Purchases**: Buyers can place orders and pay using Bitcoin.
- **Escrow System**: When a transaction is initiated, Bitcoin payments are held in escrow until both the buyer and seller confirm completion.
- **Reputation System**: After completing a transaction, both parties can leave feedback.

## Requirements

- **Python**: 3.x or higher
- **Django**: A web framework for building the backend.
- **SQLite**: A lightweight database system for development.
- **Bitcoin Payment API**: Integration with Bitcoin payment processing.

You can install the required libraries with:

```bash
pip install -r requirements.txt
```

## Future Improvements

- **Decentralized Storage**: Explore integrating decentralized file storage solutions like IPFS to host product images and user data securely.
- **Advanced Escrow & Smart Contracts**: Implement more sophisticated smart contract features using platforms like Ethereum or Lightning Network for Bitcoin.
- **Mobile Application**: Develop a mobile app for better accessibility and ease of use.
- **More Cryptocurrency Support**: Extend support for other cryptocurrencies beyond Bitcoin.



## Acknowledgments

- **Bitcoin**: For providing the foundation for decentralized transactions.
- **Django**: For the robust web framework used to power the backend.
- **SQLite**: For providing an easy-to-use database solution during development.


