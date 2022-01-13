from __future__ import annotations
from collections.abc import Iterable


class remember:
    """The singleton class"""
    _shared_data = {}

    def __init__(self, cls):
        self.cls = cls

    def __call__(cls, *args, **kwargs):
        try:
            return remember._shared_data[args]
        except KeyError:
            if len(args) == 1:
                args = int(''.join(map(str, args)))
                ret = remember._shared_data[args] = cls
            else:
                ret = remember._shared_data[args] = cls
            return ret
    
    def __str__(self):
        return str(self._shared_data.keys()) # Returns the attribute dictionary for printing

    def __iter__(self):
        return iter(self._shared_data.keys())

    def __getitem__(self, item):
        return self._shared_data[item]

@remember
class A:
    def __init__(self, x,y=0,z=0):
        pass

# Tests:
a = A(1)
b = A(2,3)
c = A(4,5,6)
d = A(1)

print(A[1] is a is d)
print(A[2,3] is b)
print(A[4,5,6] is c)
print( {x for x in A}, {1, (2,3), (4,5,6)} )
