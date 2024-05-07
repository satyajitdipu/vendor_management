# Vendor Management System

The Vendor Management System is a Django web application for managing vendors, purchase orders, and vendor performance metrics.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your_username/vendor_management_system.git
   cd vendor_management_system
   ```
2. Make A Enviroment 
    ```
    python -m venv venv
    source venv/bin/activate
    ```
3. Run Migration 
    ```
    python manage.py migrate
    ```
4. Start the development server

    ```
    Start the development server
    ```
## API Endpoints:

    - POST /api/vendors/: Create a new vendor.
    - GET /api/vendors/: List all vendors
    - GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details
    - PUT /api/vendors/{vendor_id}/: Update a vendor's details
    - DELETE /api/vendors/{vendor_id}/: Delete a vendor.
## Purchase Order API:
    - POST /api/purchase_orders/: Create a purchase order.
    - GET /api/purchase_orders/: List all purchase orders.
    - GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
    - PUT /api/purchase_orders/{po_id}/: Update a purchase order.
    - DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

## Vendor Performance API:
    - GET /api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics.