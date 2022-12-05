from math import sqrt


class MyStack(object):

    def __init__(self, size: int):
        self.MyStack = []
        self.size = size

    def is_prime(self, number: int) -> bool:
        if type(number) != int:
            raise TypeError("The number should be an integer")
        if number < 2:
            return False
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def add(self, element: int):
        if self.measure() == self.size:
            raise MemoryError("MyStack is already full")
        if not self.is_prime(element):
            raise ValueError("The integer must by prime")
        self.MyStack.append(element)

    def measure(self) -> int:
        return len(self.MyStack)

    def is_empty(self) -> bool:
        return self.measure() == 0

    def top(self) -> int:
        if self.is_empty():
            raise ValueError("MyStack is empty")
        return self.MyStack[-1]

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("MyStack is empty")
        result = self.MyStack[-1]
        self.MyStack = self.MyStack[0:-1]
        return result

    def __str__(self):
        return str(self.MyStack)
