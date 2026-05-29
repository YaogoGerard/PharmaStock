# =============================================================================
# Menu fonctions
# author: @yaroleana7-maker
# =============================================================================

from utils import display_separator, input_float, input_integer
from products import Product
from medication import Medication
from parapharmacy import ParapharmacyProduct, PARA_CATEGORIES


def add_product(stock: list) -> None:
    display_separator("ADD A PRODUCT")
    print(" 1. Medication")
    print(" 2. Parapharmacy Product")
    choice = input(" Your choice: ").strip()

    name = input(" Product name: ").strip()
    price = input_float(" Price (FCFA): ")
    quantity = input_integer(" Quantity: ")

    if choice == "1":
        pres_input = input(" Prescription required? (y/n): ").strip().lower()
        prescription = pres_input == "y"
        expiration = input(" Expiration date (DD/MM/YYYY): ").strip()
        product = Medication(name, price, quantity, prescription, expiration)
    elif choice == "2":
        print(f" Available categories: {', '.join(PARA_CATEGORIES)}")
        category = input(" Category: ").strip()
        product = ParapharmacyProduct(name, price, quantity, category)
    else:
        print(" ❌ Invalid choice.")
        return

    stock.append(product)
    print(f"\n '{name}' added to stock.")


def display_stock(stock: list) -> None:
    display_separator("CURRENT STOCK")
    if not stock:
        print(" The stock is empty.")
        return

    counters = {"medications": 0, "parapharmacy": 0, "others": 0}

    for i, product in enumerate(stock):
        print(f"\n [{i + 1}]")
        print(" " + product.display().replace("\n", "\n "))

        if product.is_low_stock():
            print(" LOW STOCK!")

        if isinstance(product, Medication):
            counters["medications"] += 1
        elif isinstance(product, ParapharmacyProduct):
            counters["parapharmacy"] += 1
        else:
            counters["others"] += 1

        display_separator()

    print(f"\n Total: {len(stock)} product(s)")
    print(
        f" Medications: {counters['medications']} | Parapharmacy: {counters['parapharmacy']}"
    )


def sell_product(stock: list) -> None:
    display_separator("SELL A PRODUCT")
    if not stock:
        print(" The stock is empty.")
        return

    for i, product in enumerate(stock):
        print(
            f" [{i + 1}] {product.get_name()} — {product.get_price()} FCFA — Stock: {product.get_quantity()}"
        )

    try:
        index = int(input("\n Product number to sell: ")) - 1
        if index < 0 or index >= len(stock):
            print(" ❌ Invalid number.")
            return
    except ValueError:
        print(" ❌ Invalid input.")
        return

    product = stock[index]

    if isinstance(product, Medication) and product.get_prescription_required():
        confirm = (
            input(" This medication requires a prescription. Confirm? (y/n): ")
            .strip()
            .lower()
        )
        if confirm != "y":
            print(" ❌ Sale cancelled.")
            return

    quantity_sold = input_integer(" Quantity to sell: ")

    if quantity_sold > product.get_quantity():
        print(f" Insufficient stock ({product.get_quantity()} available).")
        return

    product.set_quantity(product.get_quantity() - quantity_sold)
    total = quantity_sold * product.get_price()

    print("\n Sale completed!")
    print(f" Product: {product.get_name()}")
    print(f" Quantity: {quantity_sold}")
    print(f" Total: {total} FCFA")

    if product.is_low_stock():
        print(f" Warning: low stock ({product.get_quantity()} remaining)")


def show_alerts(stock: list) -> None:
    display_separator("ALERTS")
    alerts = {"expired": [], "low_stock": []}

    for product in stock:
        if isinstance(product, Medication) and product.is_expired():
            alerts["expired"].append(product.get_name())
        if product.is_low_stock():
            alerts["low_stock"].append(
                f"{product.get_name()} ({product.get_quantity()} remaining)"
            )

    if alerts["expired"]:
        print("\n ❌ EXPIRED MEDICATIONS:")
        for name in alerts["expired"]:
            print(f" - {name}")
    else:
        print("\n No expired medications.")

    if alerts["low_stock"]:
        print("\n LOW STOCK:")
        for info in alerts["low_stock"]:
            print(f" - {info}")
    else:
        print(" All stocks are sufficient.")


def search_product(stock: list) -> None:
    display_separator("SEARCH PRODUCT")
    term = input(" Name to search: ").strip().lower()

    results = [p for p in stock if term in p.get_name().lower()]

    if not results:
        print(f" No product found for '{term}'.")
        return

    print(f"\n {len(results)} result(s):\n")
    for product in results:
        print(" " + product.display().replace("\n", "\n "))
        display_separator()
