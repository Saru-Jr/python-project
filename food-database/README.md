# Food Database Project

## Overview
This project is designed to manage a database of food items, including their nutritional information and cost. It provides a structured way to store and retrieve data related to food.

## Database Structure
The database consists of the following tables:

- **Food Items**
  - `id`: Primary key
  - `name`: Name of the food item
  - `calories`: Number of calories in the food item
  - `vitaminA`: Percentage of Vitamin A
  - `vitaminC`: Percentage of Vitamin C
  - `cost`: Cost of the food item

## Setup Instructions
1. Create a new database in your SQL environment.
2. Run the SQL statements in `src/database/schema.sql` to create the necessary tables.
3. Use the queries in `src/database/queries.sql` to insert, update, and retrieve food items.
4. Run the initial migration script located in `src/migrations/initial.sql` to set up the database structure.
5. Use the test queries in `tests/test_queries.sql` to validate the functionality of the SQL queries.

## Usage
You can interact with the database using the provided SQL queries to manage food items effectively.