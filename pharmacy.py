import csv
import os
from datetime import date, datetime
STOCK_FILE = "stock.csv"
PARA_CATEGORIES = ("hygiene", "cosmetic", "nutrition", "medical equipment")
LOW_STOCK_THRESHOLD = 5
class Product:
    """Base class representing a pharmacy product."""
    def __init__(self, name: str, price: float, quantity: int):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    def get_name(self) -> str:
        return self.__name
    def get_price(self) -> float:
        return self.__price
    def get_quantity(self) -> int:
        return self.__quantity
    def set_quantity(self, new_quantity: int) -> None:
        if new_quantity >= 0:
            self.__quantity = new_quantity
    def set_price(self, new_price: float) -> None:
        if new_price > 0:
            self.__price = new_price
    def is_low_stock(self) -> bool:
        return self.__quantity <= LOW_STOCK_THRESHOLD
    def display(self) -> str:
        return (
            f"Product: {self.__name}\n"
            f"Price: {self.__price} FCFA\n"
            f"Stock: {self.__quantity} units"
        )
    def to_csv(self) -> list:
        return ["Product", self.__name, self.__price, self.__quantity, "", "", ""]

class Medication(Product):
    """Class representing a medication."""
    def __init__(
        self,
        name: str,
        price: float,
        quantity: int,
        prescription_required: bool,
        expiration_date: str,
    ):
        super().__init__(name, price, quantity)
        self.__prescription_required = prescription_required
        self.__expiration_date = expiration_date
    def get_prescription_required(self) -> bool:
        return self.__prescription_required
    def get_expiration_date(self) -> str:
        return self.__expiration_date
    def is_expired(self) -> bool:
        try:
            expiration = datetime.strptime(self.__expiration_date, "%d/%m/%Y").date()
            return expiration < date.today()
        except ValueError:
            return False
    def display(self) -> str:
        prescription = "Yes" if self.__prescription_required else "No"
        expired = " EXPIRED" if self.is_expired() else ""
        return (
            f"Medication: {self.get_name()}\n"
            f"Price: {self.get_price()} FCFA\n"
            f"Stock: {self.get_quantity()} units\n"
            f"Prescription Required: {prescription}\n"
            f"Expiration: {self.__expiration_date}{expired}"
        )
     def to_csv(self) -> list:
        return [
            "Medication",
            self.get_name(),
            self.get_price(),
            self.get_quantity(),
            self.__prescription_required,
            self.__expiration_date,
            "",
        ]
