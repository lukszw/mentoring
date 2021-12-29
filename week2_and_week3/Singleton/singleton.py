from typing import Dict

class Singleton:
    """The singleton class"""
    
    _shared_data: Dict[str, str] = {}

    def __init__(self, **kwargs):
        Singleton._shared_data.update(kwargs)
    
    def __str__(self) -> str:
        return str(self._shared_data)

    def __getitem__(self, item) -> str:
        print(type(self._shared_data[item]))
        return self._shared_data[item]


# Let's create a singleton object and add our first acronym
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
    
# Print the object:
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym
y = Singleton(SNMP = "Simple Network Management Protocol")

# Print the object:
print(y["HTTP"])


