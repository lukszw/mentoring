from math import pi


class Circle:
    """
    Class that creates and calculate Circle area and circumference

    Variable:
    - radius: it's circle radius needed to calculation

    Methods:
    - area(): calculates area of the circle
    - circumference(): calculates circumference of the circle

    Use:
    c1 = Circle(radius)
    """
    PI = pi

    def __init__(self, radius: float) -> None:
        self._radius = radius

    def __str__(self) -> str:
        """String representation of the square"""
        return f"Radius is: {self._radius}"

    def area(self) -> float:
        """Calculates area of the circle"""
        return Circle.PI * (self._radius ** 2)

    def circumference(self) -> float:
        """Calculates circumference of the circle"""
        return 2 * Circle.PI * self._radius
        