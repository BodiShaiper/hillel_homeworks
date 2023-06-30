from HW10.computer import Computer


class Laptop(Computer):
    def __init__(self, name: str, price: int, brand: str, processor: str, display_size: float):
        super().__init__(name, price, brand, processor)
        self.display_size = display_size

    def describe(self):
        super().describe()
        print(f"Display Size: {self.display_size} inches")

    def calculate_discount(self):
        discount = super().calculate_discount()
        return discount + 20


if __name__ == '__main__':
    laptop = Laptop("Gaming", 2000, "GHI Brand", "Intel i9", 15.6)
    laptop.describe()
    print(f"Discount: ${laptop.calculate_discount()}")
    print(f"Final price: ${laptop.get_final_price()}")
