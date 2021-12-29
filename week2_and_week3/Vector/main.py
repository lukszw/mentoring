from __future__ import annotations
import math

import numpy as np


class Vector:
    """Class that creates Vector and vectors calculation"""
    def __init__(self, *args) -> None:
        try:
            self.x, self.y, self.z = args if len(args) == 3 else args[0]
            self.values = [self.x, self.y, self.z]
        except ValueError:
            raise ValueError("Give single iterable of (x, y, z) or pass them as *args")
            
    def __add__(self, other_v: Vector) -> Vector:
        """Adding two vectors"""
        if isinstance(other_v, Vector):
            return Vector([a + b for a, b in zip(self.values, other_v.values)])
        else:
            raise ValueError("Supports only Vector + Vector, please provide Vector")

    def __sub__(self, other_v: Vector) -> Vector:
        """Subtraction two vectors"""
        if isinstance(other_v, Vector):
            return Vector([a - b for a, b in zip(self.values, other_v.values)])
        else:
            raise ValueError("Supports only Vector - Vector, please provide Vector")

    def __eq__(self, other_v: Vector) -> bool:
        """Methods for checking if Vector1 == Vector2"""
        return self.values == other_v.values

    def __str__(self) -> str:
        """String representation of the vector, usage: <1, 2, 3>"""
        return f"<{str(', '.join(map(str, self.values)))}>"

    def to_tuple(self) -> tuple:
        """Create tuple from vector values"""
        return tuple(self.values)

    def dot(self, other_v: Vector) -> float:
        """Creating dot product with two Vectors"""
        if isinstance(other_v, Vector):
            return sum(a * b for a, b in zip(self.values, other_v.values))
        else:
            raise ValueError("Need to be a vector")
        
    @property
    def magnitude(self) -> float:
        """Calculates magnitude"""
        return math.sqrt(sum(x*x for x in self.values))

    def cross(self, other_v: Vector) -> Vector:
        """Calculating cross with two vectors"""
        return Vector(np.cross(self.values, other_v.values))


# List of vectors
vector_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

# Vectors
v1 = Vector(vector_list[0])
v2 = Vector(vector_list[1])
v3 = Vector(*vector_list[2])

# Checking:
print(v1 + v2)
print(v1 - v2)
print(v1 == v3)
print(v1.to_tuple())
print(v1.magnitude)
print(v1.cross(v2))
print(v1.dot(v2))
