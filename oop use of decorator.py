def log_decorator(func):              
    def wrapper(*args, **kwargs):
        print(f"Calling method '{func.__name__}' with arguments {args[1:]}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned {result}")
        return result
    return wrapper
a = int(input('Enter first number'))
b = int(input('enter second number'))
class Calculator:
    @log_decorator    
    def add(self, a, b):
        return a + b

    @log_decorator
    def subtract(self, a, b):
        return a - b

    @log_decorator
    def multiply(self, a, b):
        return a * b

    @log_decorator
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
  
#   Using the Calculator class
calc = Calculator()
calc.add(a, b)
calc.subtract(a, b)
calc.multiply(a, b)
calc.divide(a, b)
