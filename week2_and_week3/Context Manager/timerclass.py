from typing import Optional, Type
from types import TracebackType
from time import perf_counter, sleep


class Timer:
    def __init__(self) -> None:
        print("Initialized and start counting")

    def __enter__(self) -> float:
        self.start_time = perf_counter()
        return lambda: self.end_time - self.start_time


    def __exit__(
        self, 
        exc_type: Optional[Type[BaseException]], 
        exc_value: Optional[BaseException], 
        exc_tb: Optional[TracebackType]
        ) -> Optional[bool]:
        self.end_time = perf_counter()


with Timer() as timer:
    sleep(1)

print(f"Time it takes: {timer()} sec.")