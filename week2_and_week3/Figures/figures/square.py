from .rectangle import Rectangle

class Square(Rectangle):
    """
    Class that creates square and calculate area and circumference

    Variables:
    - a: side of the square

    Methods:
    - area(): calculate area of the square
    - circumference(): calculate circumference of the square

    Use:
    s1 = Square(a)
    """
    def __init__(self, a: float) -> None:
        """Super from rectangle(a, b)"""
        super().__init__(a, a)

    def __str__(self) -> str:
        """String representation of the square"""
        return f"Side of the square is equal to: {self._a}"

    def area(self) -> float:
        """Calculates area of the square inherited from rectangle"""
        return super().area()

    def circumference(self) -> float:
        """Calculates circumference of the square inherited from rectangle"""
        return super().circumference()
