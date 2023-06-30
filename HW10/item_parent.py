from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def describe(self):
        print(f"This is a {self.name}.")

    @abstractmethod
    def calculate_discount(self):
        pass


if __name__ == '__main__':
    item = Item("Generic Item", 100)
    item.describe()
    print(f"Discount: ${item.calculate_discount()}")
