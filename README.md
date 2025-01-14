<h1>Django Ecommerce Website</h1>



 <h4>Product Management System</h4>

 Overview

The **Product Management System** is a Django-based web application designed to manage products and categories efficiently. This project provides a streamlined way for users to handle product inventories, organize them into categories, and manage the overall structure of a retail or e-commerce platform. 

## Features

- **Category Management**: Create, view, update, and delete product categories.
- **Product Management**: Manage products with details like name, description, price, stock quantity, and category association.
- **Database Integration**: Efficient storage and retrieval of product and category data using Django's ORM.
- **Admin Interface**: Leverage Django's built-in admin panel for easy management of data models.
- **Scalability**: Structured to handle a growing number of products and categories.

## Technology Stack

- **Backend**: Django (Python)
- **Database**: SQLite (configurable for other databases)
- **Frontend**: HTML, CSS (for basic templates)
- **Version Control**: Git

## Installation and Setup
```markdown

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/product-management-system.git
   cd product-management-system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**: Visit `http://localhost:8000` in your web browser.

## Usage

- **Admin Panel**: Access the admin panel at `/admin/` to manage categories and products.
- **Category Management**: Add, edit, and delete categories through the admin interface or programmatically using the provided functions in `categories.py`.
- **Product Management**: Manage products similarly through the admin interface or the functions in `products.py`.

## Project Structure

```
product-management-system/
│
├── categories.py         # Category model and related functions
├── products.py           # Product model and related functions
├── settings.py           # Project settings configuration
├── db.sqlite3            # SQLite database file (default)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Configuration

- **Category and Product Limits**: Configure limits for categories and products in the `settings.py` file:
  ```python
  CATEGORY_LIMIT = 50  # Max categories allowed
  PRODUCT_LIMIT = 100  # Max products per category
  ```
- **Database**: Default setup uses SQLite. Update `settings.py` to use other databases like PostgreSQL or MySQL as needed.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```

