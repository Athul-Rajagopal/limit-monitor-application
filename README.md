# Limit Monitor Application

## Overview
This is a Django application for monitoring limits based on fetched weather data. Users can define criteria such as temperature, humidity, etc., and the application evaluates whether these criteria are met based on the fetched weather data. It also provides CRUD (Create, Read, Update, Delete) operations for managing limit records.

## Features
- **Monitoring Logic**: Implements logic to compare fetched weather data with user-defined criteria and trigger actions if conditions are met.
- **ERD**: Provides an Entity-Relationship Diagram (ERD) to visualize the database schema.
- **CRUD Operations**: Allows users to perform CRUD operations on limit records.
- **Status Update**: Defines conditions for updating the status of records and implements a scheduler task to periodically check and update records.

## Implementation Details
### Monitoring Logic
- Compares fetched weather data with user-defined criteria using comparison operators (<, >, <=, >=, ==).
- Determines if conditions are met for the given frequency (day, month, year).
- Triggers actions (e.g., updating the database, sending notifications) if conditions are satisfied.

### CRUD Operations
- **Create**: Users can add new limit records to the database using a form.
- **Read**: Displays all records in a tabular format with options to view details and perform edit/delete operations on each record.
- **Update**: Provides a form to edit existing records and updates them in the database.
- **Delete**: Allows users to delete records from the database.

### Status Update
- Defines conditions for updating the status of records, such as reaching a certain date or meeting specific criteria.
- Implements a scheduler task using Django's built-in task scheduler or external libraries like Celery to periodically check and update records' status in the database.


## Files and Directories
- **/monitor**: Django app directory containing models, forms, views, and templates related to limit monitoring.
- **/static**: Directory for storing static files such as CSS, JavaScript, and images.
- **/templates**: Contains HTML templates for rendering user interface components.
- **manage.py**: Django management script for administrative tasks.
- **README.md**: This file, providing an overview and instructions for the project.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install Python and Django if not already installed.
3. Create a virtual environment and activate it.
4. Install dependencies using `pip install -r requirements.txt`.
5. Run migrations to create database tables: `python manage.py migrate`.
6. Start the development server: `python manage.py runserver`.
7. Access the application at `http://localhost:8000/`.

## Usage
1. Access the home page to view the landing page.
2. Register an account or log in if you haven't already done so.
3. Navigate to the limit monitoring section to add, view, edit, or delete limit records.
4. Configure limit criteria and frequency for monitoring.
5. Monitor the status of records and update them based on defined conditions.

## Contributors
- Athul Rajagopalan P


## License
This project is licensed under the [MIT License](LICENSE).
