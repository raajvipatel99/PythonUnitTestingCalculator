from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division

class Calculator:
    result = 0

    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = Addition.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction.subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Division.division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication.multiplication(a, b)
        return self.result