class A:
    def call_name(self) -> None:
        print("I am class A and the name is Mario")


class B(A):
    def call_name(self) -> None:
        print("I am class B and the name is Alex")


class C(A):
    def call_name(self) -> None:
        print("I am class C and the name is Ola")


class D(B, C):
    pass


class E(C, B):
    pass


# Create a class:
new_obj = D()
new_obj2 = E()

# Check what will be printed:
new_obj.call_name()
new_obj2.call_name()

# Check the MRO - linearization
print(D.mro())
print(E.mro())

# So the linearization is as follow: Class D -> Class B -> Class C -> Class A -> object
# When we change class D(C, B) then : Class D -> Class C -> Class B -> Class A -> object
