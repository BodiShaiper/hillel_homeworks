from HW11.abstraction import Shape


# Inheritance: Circle inherits from Shape
# Polymorphism: The area method is overridden with a specific implementation.
class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


if __name__ == '__main__':
    circle_sample = Circle("Purple", 5)
    circle_sample.describe()  # Polymorphism: The describe method is called on the Circle object.
    print(circle_sample.area())  # Polymorphism: The area method is called to calculate the area of the circle object.
