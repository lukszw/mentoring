from typing import Generator

def gen(n: float) -> Generator[float, None, None]:
    for i in range(n):
        yield i ** 2

my_generator = gen(10)

# Check the output using next()
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))

# Creating a generator that receives number to the power of 2
my_gen = (i**2 for i in range(15))

# Check the output using for loop
# for i in my_gen:
#     print(i)

# StopIteration Error
#print(next(my_gen))


# Check with list:
my_list = [1,2,3,4,5]
# next(my_list) # -> 'list' object is not an iterator

my_list_new = iter(my_list)
print(next(my_list_new))

