from HW10.phone import Phone


class PhoneButtons(Phone):
    def __init__(self, name: str, price: int, brand: str, model: str, os: str, os_version: float, camera: bool,
                 ik_port: bool, bluetooth: bool):
        super().__init__(name, price, brand, model, os, os_version)
        self.camera = camera
        self.ik_port = ik_port
        self.bluetooth = bluetooth

    def describe(self):
        super().describe()
        print(f"Camera: {self.camera}")
        print(f"IK-Port: {self.ik_port}")
        print(f"Bluetooth: {self.bluetooth}")

    def calculate_discount(self):
        discount = super().calculate_discount()
        return discount + 29


if __name__ == '__main__':
    phone_buttons = PhoneButtons("Phone", 700, "Nokia", "6300", "Android", 1.0, True, True, False)
    phone_buttons.describe()
    print(f"Discount: ${phone_buttons.calculate_discount()}")
    print(f"Final price: ${phone_buttons.get_final_price()}")
