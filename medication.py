# =============================================================================
# medication class
# author: @Yams-tech
# =============================================================================

from datetime import date, datetime
from products import Product


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
