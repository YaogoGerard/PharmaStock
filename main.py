# =============================================================================
# Main menu and program entry point
# author: @YaogoGerard
# =============================================================================

from datetime import date
from utils import display_separator, save_stock, load_stock
from menu import add_product, display_stock, sell_product, show_alerts, search_product


def display_menu() -> None:
    display_separator("PHARMACY — MAIN MENU")
    print(" 1. Display stock")
    print(" 2. Add a product")
    print(" 3. Sell a product")
    print(" 4. Alerts (expired / low stock)")
    print(" 5. Search product")
    print(" 6. Save stock")
    print(" 0. Exit")
    display_separator()


def main() -> None:
    print("\n Welcome in PharmaStock")
    print(f" Date: {date.today().strftime('%d/%m/%Y')}")

    stock: list = load_stock()

    running = True
    while running:
        display_menu()
        choice = input(" Your choice: ").strip()

        if choice == "1":
            display_stock(stock)
        elif choice == "2":
            add_product(stock)
        elif choice == "3":
            sell_product(stock)
        elif choice == "4":
            show_alerts(stock)
        elif choice == "5":
            search_product(stock)
        elif choice == "6":
            save_stock(stock)
        elif choice == "0":
            save_stock(stock)
            print("\n Goodbye!\n")
            running = False
        else:
            print(" ❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
