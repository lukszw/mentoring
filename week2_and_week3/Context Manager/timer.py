from typing import Generator
from contextlib import contextmanager
from time import sleep, perf_counter

@contextmanager
def timer() -> Generator[float, None, None]:
    print("Initialized and start counting")
    start_time = perf_counter()
    yield lambda: perf_counter() - start_time


with timer() as timer:
    sleep(1)

print(f"Time it takes: {timer()} sec.")
