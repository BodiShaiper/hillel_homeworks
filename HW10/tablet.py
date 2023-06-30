from HW10.electronics import Electronics


class Tablet(Electronics):
    def __init__(self, name: str, price: int, brand: str, model: str, bluetooth: bool, display_size: float):
        super().__init__(name, price, brand)
        self.model = model
        self.display_size = display_size
        self.bluetooth = bluetooth

    def describe(self):
        super().describe()
        print(f"Model: {self.model}")
        print(f"Bluetooth: {self.bluetooth}")
        print(f"Display Size: {self.display_size}")

    def calculate_discount(self):
        discount = super().calculate_discount()
        return discount + 25


if __name__ == '__main__':
    tablet = Tablet("Tablet", 4400, "Samsung", "Galaxy A-2020", True, 10.4)
    tablet.describe()
    print(f"Discount: ${tablet.calculate_discount()}")
    print(f"Final price: ${tablet.get_final_price()}")
