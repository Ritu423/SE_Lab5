"""
Inventory management system module.
Provides functions to manage stock, including adding, removing, saving,
loading, and reporting inventory items.
"""

import json
import logging
from datetime import datetime
import ast

logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def add_item(stock_data, item, qty, logs=None):
    """Add or update an item in the inventory."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types: item=%s, qty=%s", type(item), type(qty))
        return logs
    stock_data[item] = stock_data.get(item, 0) + qty
    message = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(message)
    logging.info("%s", message)
    return logs


def remove_item(stock_data, item, qty):
    """Remove a specific quantity of an item from the inventory."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
                logging.info("Removed '%s' from inventory.", item)
        else:
            logging.warning("Tried to remove non-existent item: %s", item)
    except KeyError as e:
        logging.error("KeyError occurred while removing item: %s", e)
    except TypeError as e:
        logging.error("TypeError occurred: %s", e)


def get_qty(stock_data, item):
    """Return the quantity of a specific item in the inventory."""
    return stock_data.get(item, 0)


def load_data(filename="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
            if data.strip():
                stock_data = ast.literal_eval(data)
                logging.info("Data loaded successfully from %s", filename)
                return stock_data
            logging.warning("No data found in %s", filename)
            return {}
    except FileNotFoundError:
        logging.error("File not found: %s", filename)
        return {}
    except (ValueError, SyntaxError) as e:
        logging.error("Error parsing data: %s", e)
        return {}


def save_data(stock_data, filename="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
        logging.info("Data saved successfully to %s", filename)
    except (OSError, TypeError) as e:
        logging.error("Error saving data: %s", e)


def print_data(stock_data):
    """Print the inventory report to the console."""
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Return a list of items with quantity below the threshold."""
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    if low_items:
        logging.info("Low stock items found: %s", low_items)
    return low_items


def main():
    """Main execution function to demonstrate inventory operations."""
    stock_data = {}
    logs = []
    logs = add_item(stock_data, "apple", 10, logs)
    logs = add_item(stock_data, "banana", 2, logs)
    logs = add_item(stock_data, "orange", 0, logs)
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)
    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print("Low items:", check_low_items(stock_data))
    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)
    logging.info("Inventory system executed successfully.")


if __name__ == "__main__":
    main()
