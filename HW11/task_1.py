# Encapsulation
class Shape:
    def __init__(self, color):
        self._color = color  # Encapsulation: The color attribute is encapsulated.

    @property
    def color(self):
        return self._color  # Encapsulation: Getter method provides access to the color attribute.

    @color.setter
    def color(self, value):
        self._color = value  # Encapsulation: Setter method allows modification of the color attribute.

    def area(self):
        pass


# Inheritance: The Rectangle class inherits from the Shape class.
# Hiding: The width attribute is hidden as a private attribute.
# Polymorphism: The area method is overridden with a specific implementation.
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.__width = width
        self._height = height  # Encapsulation

    @property
    def width(self):
        return self.__width  # Encapsulation

    @width.setter
    def width(self, value):
        self.__width = value  # Encapsulation

    @property
    def height(self):
        return self._height  # Encapsulation

    @height.setter
    def height(self, value):
        self._height = value  # Encapsulation

    def area(self):
        return self.width * self.height


# Usage:
rect = Rectangle("Blue", 5, 10)
print(rect.color)  # Encapsulation: Accessing the color attribute using the property.
rect.color = "Green"  # Encapsulation: Modifying the color attribute using the property.
print(rect.color)
print(rect.area())  # Polymorphism: The overridden area method is called to calculate the area of the rectangle.
