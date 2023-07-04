from HW10.electronics import Electronics


class Computer(Electronics):
    def __init__(self, name: str, price: int, brand: str, processor: str):
        super().__init__(name, price, brand)
        self.processor = processor

    def describe(self):
        super().describe()
        print(f"Processor: {self.processor}")

    def calculate_discount(self):
        discount = super().calculate_discount()
        return discount + 15


if __name__ == '__main__':
    computer = Computer("Desktop", 1500, "DEF Brand", "Intel i7")
    computer.describe()
    print(f"Discount: ${computer.calculate_discount()}")
    print(f"Final price: ${computer.get_final_price()}")
