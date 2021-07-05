from Addition import Addition

class Calculator:
    result = 0

    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = Addition.addition(a, b)
        return self.result
