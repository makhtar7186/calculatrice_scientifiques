from calculator.calculator import Calculator
import math

class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.result = 0
    
    def power(self, a, b):
        self.result = a ** b
        return self.result
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        self.result = a ** 0.5
        return self.result
    
    def logarithm(self, a, base=10):
        if a <= 0:
            raise ValueError("Cannot calculate logarithm of non-positive numbers.")
        if base <= 1:
            raise ValueError("Base must be greater than 1.")
        import math
        self.result = math.log(a, base)
        return self.result
    
    def sin(self, a):
        self.result = math.sin(a)
        return self.result
    
    def cos(self, a):
        self.result = math.cos(a)
        return self.result
    
    def tan(self, a):
        self.result = math.tan(a)
        return self.result

    def evaluate(self, expression: str):
        try:
            return eval(expression)
        except Exception:
            raise ValueError("Invalid expression")

    def ans(self):
        return self.result