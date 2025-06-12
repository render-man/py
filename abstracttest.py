from abc import ABC, abstractmethod
from typing import Protocol
class Base:
    def __init__(self):
        pass

    def __str__(self):
        return "a"

    @abstractmethod
    def cal(self):
        pass

class Child(Base):
    def cal(self):
        return 10

    def __str__(self):
        return super().__str__() + "10"

    def do(self)-> None:
        print("{0} {1}".format(10, 100))


class Func(Protocol):
    def do(self) -> None:
        pass

def dothing(a: Func):
    a.do()


dothing(Child())

a = Child()
b = Child()

print(a,  "bruh")
