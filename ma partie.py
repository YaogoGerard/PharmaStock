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