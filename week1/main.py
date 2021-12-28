import os
from dotenv import load_dotenv, find_dotenv

# Znajdz .env
load_dotenv(find_dotenv())

# TODO: Zadanie 4
print(f"Wartość zmiennej środowiskowej: {os.environ.get('TEST')}")
print(f"Pierwsza litera: {os.environ.get('TEST')[0]}")
print(f"Ostatnia litera: {os.environ.get('TEST')[-1]}")
print(f"Ostatnia litera: {os.environ.get('TEST')[-1]}")
print(f"Długość: {len(os.environ.get('TEST'))}")

# TODO: Zadanie 5
env_list = [item for item in os.environ.get('TEST')]
print(f"Lista zawierająca wszystkie litery osobno: {env_list}")
print(f"Posortowana alfabetycznie lista: {sorted(env_list)}")
print(f"Tylko niepowtarzające się litery: {set(env_list)}")

# TODO: Zadanie 6
new_dict = {k: k**2 for k in range(1, 16)}
print(f"Słownik z key: liczbą i value: potęgą liczby: {new_dict}")

# TODO: Zadanie 7
print(f"Wynik [1] * 3: {[1] * 3}")
print(f"Wynik [[1,2]] * 3: {[[1,2]] * 3}")
print(f"Wynik [[1,2] * 3]: {[[1,2] * 3]}")


# TODO: Zadanie 8
def fibo(n: int) -> int:
    if n in {0, 1}:
        return n
    else:
        fibo_prev, fibo_num = 0, 1
        for _ in range(2, n + 1):
            fibo_prev, fibo_num = fibo_num, fibo_prev + fibo_num

        return fibo_num


print(fibo(6))
