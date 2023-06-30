from HW10.electronics import Electronics


class Phone(Electronics):
    def __init__(self, name: str, price: int, brand: str, model: str, os: str, os_version: float):
        super().__init__(name, price, brand)
        self.model = model
        self.os = os
        self.os_version = os_version

    def describe(self):
        super().describe()
        print(f"Model: {self.model}")
        print(f"OS: {self.os}")
        print(f"OS Version: {self.os_version}")

    def calculate_discount(self):
        discount = super().calculate_discount()
        return discount + 10


if __name__ == '__main__':
    phone = Phone("Old phone", 1000, "XYZ Brand", "Model A", "Windows", 12.0)
    phone.describe()
    print(f"Discount: ${phone.calculate_discount()}")
    print(f"Final price: ${phone.get_final_price()}")
