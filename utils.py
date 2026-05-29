# =============================================================================
# Utility functions
# author: @CAR-id13
# =============================================================================

import csv
import os
from product import Product
from medication import Medication
from parapharmacy import ParapharmacyProduct


STOCK_FILE = "stock.csv"


def display_separator(title: str = "") -> None:
    if title:
        print(f"\n{'=' * 50}")
        print(f" {title}")
        print(f"{'=' * 50}")
    else:
        print("-" * 50)


def input_float(message: str) -> float:
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            print(" ❌ Value must be positive.")
        except ValueError:
            print(" ❌ Please enter a valid number.")


def input_integer(message: str) -> int:
    while True:
        try:
            value = int(input(message))
            if value >= 0:
                return value
            print(" ❌ Value must be positive or zero.")
        except ValueError:
            print(" ❌ Please enter a valid integer.")


def save_stock(stock: list) -> None:
    with open(STOCK_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "type",
                "name",
                "price",
                "quantity",
                "prescription",
                "expiration",
                "category",
            ]
        )
        for product in stock:
            writer.writerow(product.to_csv())
    print(f" Stock saved to '{STOCK_FILE}'.")


def load_stock() -> list:
    stock = []
    if not os.path.exists(STOCK_FILE):
        return stock

    with open(STOCK_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                product_type = row["type"]
                name = row["name"]
                price = float(row["price"])
                quantity = int(row["quantity"])

                if product_type == "Medication":
                    prescription = row["prescription"] == "True"
                    expiration = row["expiration"]
                    stock.append(
                        Medication(name, price, quantity, prescription, expiration)
                    )
                elif product_type == "Parapharmacy":
                    category = row["category"]
                    stock.append(ParapharmacyProduct(name, price, quantity, category))
                else:
                    stock.append(Product(name, price, quantity))
            except (KeyError, ValueError):
                continue

    print(f" {len(stock)} product(s) loaded from '{STOCK_FILE}'.")
    return stock
