import iso6346


class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        """Generates container bic code.

        Args:
            owner_code (str): Owner code.
            serial (str): Container serial number.

        Returns:
            str: An ISO 6346 container code.
        """
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @staticmethod
    def _get_next_serial():
        serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return serial

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))


    def __init__(self, owner_code, contents):
        """
        Purpose: owner_code
        """
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial()
        )
    # end alternate constructor

c1 = ShippingContainer("ESC", "Shoes")

c2 = ShippingContainer("ESC", "Fruits")
print(c1.bic, c2.bic)
