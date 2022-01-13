import time
from time import sleep
import functools


def timer(func=None, *, limit=1):
    """Decorator checks if current function runs faster than the limit"""
    def decorator_timer(func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()
            func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time

            if run_time < limit:
                return True
            else:
                return False

        return wrapper_timer

    if func is None:
        return decorator_timer

    else:
        return decorator_timer(func)


@timer(limit=1)
def foo():
    sleep(0.1)


@timer(limit=1)
def bar():
    sleep(1.1)


print(foo()) # -> True
print(bar()) # -> False
