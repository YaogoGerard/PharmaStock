# =============================================================================
# parapharmacy class
# author: @odetteyameogo2002-sketch
# =============================================================================

from products import Product


PARA_CATEGORIES = ("hygiene", "cosmetic", "nutrition", "medical equipment")


class ParapharmacyProduct(Product):
    """Class representing a parapharmacy product."""

    def __init__(self, name: str, price: float, quantity: int, category: str):
        super().__init__(name, price, quantity)
        if category.lower() in PARA_CATEGORIES:
            self.__category = category.lower()
        else:
            self.__category = "other"

    def get_category(self) -> str:
        return self.__category

    def display(self) -> str:
        return (
            f"Parapharmacy: {self.get_name()}\n"
            f"Price: {self.get_price()} FCFA\n"
            f"Stock: {self.get_quantity()} units\n"
            f"Category: {self.__category.capitalize()}"
        )

    def to_csv(self) -> list:
        return [
            "Parapharmacy",
            self.get_name(),
            self.get_price(),
            self.get_quantity(),
            "",
            "",
            self.__category,
        ]
