class Triangle:
    """
    Class that calculates triangle area and circumference:

    Variables:
    - a: it's first side of the triangle
    - b: it's second side of the triangle
    - c: it's third side of the triangle
    - h: it's height of the triangle

    Methods:
    - area(): calculates area of the triangle
    - circumference(): calculates circumference of the triangle

    Use: 
    t1 = Triangle(a, b, c, h)
    """
    def __init__(self, a: float, b: float, c: float, h: float) -> None:
        self._a = a
        self._b = b
        self._c = c
        self._h = h
        self._sides = [self._a, self._b, self._c]
        
        if sum(sorted(self._sides)[:2]) > sorted(self._sides)[-1]:
            print("Triangle can be made")
        else:
            raise ValueError("The triangle cannot be made of these sides")
    
    def __str__(self) -> str:
        """String representation of the Triangle"""
        return f"Side a: {self._a}, side b: {self._b}, side c: {self._c}, height: {self._h}"

    @staticmethod
    def check_triangle(a,b,c) -> str:
        sides = [a, b, c]
        if sum(sorted(sides)[:2]) > sorted(sides)[-1]:
            return "This triangle can be made"
        else:
            return "The triangle cannot be create of these sides"

    def area(self) -> float:
        """Calculates area of the triangle"""
        return (self._a * self._h) / 2
    
    def circumference(self) -> float:
        """Calculates circumference of the triangle"""
        return self._a + self._b + self._c
