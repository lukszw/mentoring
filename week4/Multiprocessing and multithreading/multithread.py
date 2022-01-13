"""File that checks time for Multithreading CPU-BOUND operations"""
import concurrent.futures
import time
from contextlib import contextmanager
from typing import Generator


@contextmanager
def time_it(what: str) -> Generator[None, None, None]:
    """Context manager to calculate time"""
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{what} took {time.perf_counter() - start}")


def do_something() -> int:
    """Function to make some calculations"""
    with time_it("do_something function"):
        result = 0
        for _ in range(10_000_000):
            result += 1
        return result


def main() -> int:
    """Main function"""
    with time_it("main function"):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            futures = [pool.submit(do_something) for _ in range(10)]
            for future in concurrent.futures.as_completed(futures):
                print(f"Got {future.result()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
