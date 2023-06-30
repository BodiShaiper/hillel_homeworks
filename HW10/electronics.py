from HW10.item_parent import Item


class Electronics(Item):
    def __init__(self, name: str, price: int, brand: str):
        super().__init__(name, price)
        self.brand = brand

    def describe(self):
        print(f"This is an electronic {self.name}.")
        print(f"Brand: {self.brand}")

    def calculate_discount(self):
        discount = self.price * 0.1
        return discount

    def get_final_price(self):
        final_price = self.price - self.calculate_discount()
        return final_price


if __name__ == '__main__':
    electronics = Electronics("Generic Electronics", 500, "ABC Brand")
    electronics.describe()
    print(f"Discount: ${electronics.calculate_discount()}")
    print(f"Final price: ${electronics.get_final_price()}")
