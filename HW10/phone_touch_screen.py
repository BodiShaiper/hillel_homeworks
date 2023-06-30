from HW10.phone import Phone


class PhoneTouchScreen(Phone):
    def __init__(self, name: str, price: int, brand: str, model: str, os: str, os_version: float, nfc: bool,
                 water_resistant: bool, battery: str):
        super().__init__(name, price, brand, model, os, os_version)
        self.nfc = nfc
        self.water_resistant = water_resistant
        self.battery = battery

    def describe(self):
        super().describe()
        print(f"NFC: {self.nfc}")
        print(f"Water Resistant: {self.water_resistant}")
        print(f"Battery: {self.battery}")

    def calculate_discount(self):
        discount = super().calculate_discount()
        return discount + 50


if __name__ == '__main__':
    phone_touch_screen = PhoneTouchScreen("SmartPhone", 20000, "Xiaomi", "Mi 20 Pro MAX", "Android", 15.0, True, True,
                                          "10000 mAh")
    phone_touch_screen.describe()
    print(f"Discount: ${phone_touch_screen.calculate_discount()}")
    print(f"Final price: ${phone_touch_screen.get_final_price()}")
