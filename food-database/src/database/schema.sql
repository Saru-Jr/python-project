CREATE TABLE food_items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    calories INT NOT NULL,
    vitamineA INT NOT NULL,
    vitamineC INT NOT NULL,
    cost DECIMAL(10, 2) NOT NULL
);