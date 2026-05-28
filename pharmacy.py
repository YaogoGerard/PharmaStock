def add_product (stock: list) -> None:
    display_separator ("ADD A PRODUCT")
    print(" 1. Medication")
    print(" 2. Parapharmacy Product")
    choice = input(" Your choice: ").strip()
    
    name = input(" Product name: ").strip()
    price = input_float(" Price(FCFA): ")
    quantity = input_integer ( "Quantity: ")
