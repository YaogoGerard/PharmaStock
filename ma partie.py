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
        