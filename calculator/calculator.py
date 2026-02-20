class Calculator:
    def __init__(self):
        pass

    def add(self,*numbers):
        result = sum(numbers)
        return result    
    def subtract(self, a, b):
        result = a - b
        return result
    
    def multiply(self, *numbers):
        if not numbers:
            return 0
        res = 1
        for n in numbers:
            res *= n
        result = res
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        return result
    
