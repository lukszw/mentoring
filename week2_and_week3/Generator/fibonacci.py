from typing import Generator

# Fibonacci:
def fibo(limit: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

print(list(fibo(11)))