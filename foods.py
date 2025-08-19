import sqlite3
from datetime import datetime
import random

class Food:
    def __init__(self, name, calories, vitamineA, vitamineC, cost):
        self.id = random.randint(100, 999)  # Initial 3-digit ID
        self.name = name
        self.calories = calories
        self.vitamineA = vitamineA
        self.vitamineC = vitamineC
        self.cost = cost
        self.connect_db()
        self.ensure_unique_id()  # Make sure ID is unique

    def connect_db(self):
        self.conn = sqlite3.connect('foods.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            calories INTEGER,
            vitamine_a INTEGER,
            vitamine_c INTEGER,
            cost REAL,
            created_at TIMESTAMP
        )
        ''')
        self.conn.commit()

    def is_id_taken(self, id_to_check):
        self.cursor.execute('SELECT 1 FROM foods WHERE id = ?', (id_to_check,))
        return self.cursor.fetchone() is not None

    def ensure_unique_id(self):
        while self.is_id_taken(self.id):
            self.id = random.randint(100, 999)  # Generate new ID if taken

    def save_to_db(self):
        self.cursor.execute('''
        INSERT INTO foods (id, name, calories, vitamine_a, vitamine_c, cost, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self.id, self.name, self.calories, self.vitamineA, self.vitamineC, self.cost, datetime.now()))
        self.conn.commit()

    def get_nutrition_info(self):
        return f"ID: {self.id}, Name: {self.name}, Calories: {self.calories}, Vitamine A: {self.vitamineA}%, Vitamine C: {self.vitamineC}%"

    def get_cost_info(self):
        return f"Cost: ${self.cost}"

# Get user input
name = input("Enter food name: ")
calories = int(input("Enter calories: "))
vitamineA = int(input("Enter Vitamine A (%): "))
vitamineC = int(input("Enter Vitamine C (%): "))
cost = float(input("Enter cost: $"))

# Create food item and save to database
food_item = Food(name, calories, vitamineA, vitamineC, cost)
food_item.save_to_db()

# Display information
print(food_item.get_nutrition_info())
print(food_item.get_cost_info())
print("Food item saved to database successfully.")
