from abc import ABC, abstractmethod

class A1:
    def __init__(self, c1):
        self.c1 = c1
        self.arr = [c1]

    def __str__(self):
        return f'num: {self.c1}  + arr:{self.arr}'

    def __add__(self, other):
        _new = A1(self.c1 + other.c1)
        _new.arr = self.arr + other.arr
        return _new


a1 = A1(1)
a2 = A1(2)

print(a1 + a2)

print(f"{"hehe":<10} {"haha":<10} {"bruh":<10}")

for i in range(0, 4):
    print(f"{i:<10} {i + 1000:<10} {i + 999:<10}")
