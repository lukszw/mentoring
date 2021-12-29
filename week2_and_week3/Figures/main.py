from figures.rectangle import Rectangle
from figures.square import Square
from figures.circle import Circle
from figures.triangle import Triangle

c1 = Circle(5)
print(c1)
print(f"Area of the Circle: {c1.area()}")
print(f"Circumference of the Circle: {c1.circumference()}\n")

t1 = Triangle(3, 5, 4, 4)
print(t1)
print(f"Checking sides of the triangle: {t1.check_triangle(3, 5, 4)}")
print(f"Area of the Triangle: {t1.area()}")
print(f"Circumference of the Triangle: {t1.circumference()}\n")

# Triangle cannot be made of these sides
# t2 = Triangle(3, 5, 8, 4)
# print(t2)
#print(t1.check_triangle(3, 5, 8))
# print(f"Area of the Triangle: {t2.area()}")
# print(f"Circumference of the Triangle: {t2.circumference()}")

s1 = Square(5)
print(s1)
print(f"Area of the Square: {s1.area()}")
print(f"Circumference of the Square: {s1.circumference()}\n")

r1 = Rectangle(4, 6)
print(r1)
print(f"Area of the Circle: {r1.area()}")
print(f"Circumference of the Square: {r1.circumference()}\n")

