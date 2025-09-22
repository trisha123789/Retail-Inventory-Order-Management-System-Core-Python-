# Retail-Inventory-Order-Management-System-Core-Python-
Retail Management CLI: Inventory, Orders & Payments

A command-line interface application to manage products, customers, orders, and payments for a retail store.

This project allows store managers to efficiently handle inventory, process customer orders, track payments, and generate reports — all from the terminal.
Table Structure
<img width="1085" height="551" alt="image" src="https://github.com/user-attachments/assets/fa3210a9-43e8-48ed-a606-2b5ce2b01b40" />

Features
Product Management

Add, list, and view products

Track product stock and categories

Validate SKU uniqueness and product price

Customer Management

Add, list, get, and delete customers

Store customer info: name, email, phone, city

Easy retrieval by name or ID

Order Management

Create orders with multiple products and quantities

Check stock availability before order placement

Automatically calculate total order amount

Cancel orders and restore stock

Fetch order details including customer info and order items

Payment Management

Track payments for orders

Mark payments as PAID, REFUNDED, or PENDING

Update order status based on payment

Reporting

Top-selling products

Total revenue over a period

Orders per customer

Customers with multiple orders

Tech Stack

Backend / CLI: Python 3.x, argparse, JSON

Database:Supabase

Architecture: Service layer + DAO layer with OOP

Version Control: Git & GitHub

Installation & Setup

Clone the repository:

git clone https://github.com/trisha123789/Retail-Inventory-Order-Management-System-Core-Python-.git
cd Retail-Inventory-Order-Management-System-Core-Python-


Install dependencies (if any):

pip install -r requirements.txt


Configure database:

Set up  Supabase

Update src/config.py with your DB credentials

Usage

Run the CLI:

python retail-cli.py

Example Commands

Add a product:

python retail-cli.py product add --name "Laptop" --sku "LPT123" --price 800.00 --stock 10 --category "Electronics"


List products:

python retail-cli.py product list


Add a customer:

python retail-cli.py customer add --name "Alice" --email "alice@example.com" --phone "1234567890" --city "New York"


Create an order:

python retail-cli.py order create --customer 1 --item 1:2 2:1


Cancel an order:

python retail-cli.py order cancel --order 1


Show order details:

python retail-cli.py order show --order 1

Project Structure
src/
├─ services/        # Business logic layer (OOP)
│  ├─ product_service.py
│  ├─ customer_service.py
│  ├─ order_service.py
│  └─ payment_service.py
├─ dao/             # Database access layer
│  ├─ product_dao.py
│  ├─ customer_dao.py
│  ├─ order_dao.py
│  └─ payment_dao.py
├─ config.py        # DB configuration (Supabase/Postgres)

README.md

Contributing

Fork the repository

Create your feature branch: git checkout -b feature/your-feature

Commit your changes: git commit -m "Add your feature"

Push to the branch: git push origin feature/your-feature

Open a Pull Request

License

This project is MIT Licensed — free to use and modify.
