from abc import ABC, abstractmethod


# Abstraction: Shape is an abstract base class
# Encapsulation
class Shape(ABC):
    def __init__(self, color: str):
        self._color = color  # Encapsulation: The color attribute is encapsulated.

    @property
    def color(self):
        return self._color  # Encapsulation: Getter method provides access to the color attribute.

    @color.setter
    def color(self, value):
        self._color = value  # Encapsulation: Setter method allows modification of the color attribute.

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print(f"This shape is {self.color} in color.")
