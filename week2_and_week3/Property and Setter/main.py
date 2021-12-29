class Employee:
    """Employee class"""
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    @property
    def email(self) -> str:
        """Get email based on first and last name"""
        return f"{self.fname}.{self.lname}@email.com"

    @property
    def fullname(self) -> str:
        """Get first and last name as a fullname"""
        return f"{self.fname} {self.lname}"

    @fullname.setter
    def fullname(self, name: str) -> None:
        """Set new first and last name"""
        fname, lname = name.split(" ")
        self.fname = fname
        self.lname = lname


# Initialize
e1 = Employee("Lukasz", "Szwajnoch")

# Setter (set and replace the original initialized name)
e1.fullname = "Jan Kowalski"

# Check if setter works
print(e1.fname)
print(e1.lname)
print(e1.email)
print(e1.fullname)