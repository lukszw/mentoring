class Rectangle:
    """
    Class that creates Rectangle and calculate area and circumference

    Variables:
    - a: first side of the Rectangle
    - b: second side of the Rectangle

    Methods:
    - area(): calculate area of the Rectangle
    - circumference(): calculate circumference of the Rectangle

    Use:
    s1 = Rectangle(a, b)
    """
    def __init__(self, a: float, b: float) -> None:
        self._a = a
        self._b = b

    def __str__(self) -> str:
        """String representation of the Rectangle"""
        return f"First side o the Rectangle (a): {self._a} and second side of the Rectangle (b): {self._b}"
    
    def area(self) -> float:
        """Calculates area of the Rectangle"""
        return self._a * self._b

    def circumference(self) -> float:
        """Calculates circumference of the Rectangle"""
        return (2 * self._a) + (2 * self._b)

