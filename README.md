# Vendor-Management-System
"Vendor Management System: A Django-based application for managing vendor profiles, tracking purchase orders, and evaluating vendor performance metrics. This system provides RESTful API endpoints for CRUD operations on vendors and purchase orders, along with endpoints for retrieving performance metrics. Built with Django and Django REST Framework."

# Vendor Management System

## Description
Vendor Management System is a Django-based application designed to streamline vendor management processes. It provides features for managing vendor profiles, tracking purchase orders, and evaluating vendor performance metrics. This README file provides an overview of the project structure, API endpoints, and setup instructions.

## Project Structure
- `vendor_management_system/`: Django project directory.
  - `vendor_management/`: Django app directory.
    - `models.py`: Contains Django models for Vendor and PurchaseOrder.
    - `views.py`: Contains Django views for handling API requests.
    - `serializers.py`: Contains serializers for converting Django model instances to JSON.
    - `urls.py`: Contains URL patterns for routing API requests to the appropriate views.

## API Endpoints
- **Vendor Profile Management**:
  - `POST /api/vendors/`: Create a new vendor.
  - `GET /api/vendors/`: List all vendors.
  - `GET /api/vendors/<int:pk>/`: Retrieve details of a specific vendor.
  - `PUT /api/vendors/<int:pk>/`: Update a vendor's details.
  - `DELETE /api/vendors/<int:pk>/`: Delete a vendor.
- **Vendor Performance Evaluation**:
  - `GET /api/vendors/<int:pk>/performance/`: Retrieve performance metrics for a specific vendor.
- **Purchase Order Tracking**:
  - `POST /api/purchase-orders/`: Create a new purchase order.
  - `GET /api/purchase-orders/`: List all purchase orders.
  - `GET /api/purchase-orders/<int:pk>/`: Retrieve details of a specific purchase order.
  - `PUT /api/purchase-orders/<int:pk>/`: Update a purchase order.
  - `DELETE /api/purchase-orders/<int:pk>/`: Delete a purchase order.

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory:
   ```bash
   cd vendor_management_system
