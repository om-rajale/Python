"""Create a class Calculator with two instance variables a and b. Implement instance methods to
perform addition and subtraction. Add a static method to multiply two numbers without using the
instance variables. Create an object of Calculator and demonstrate the usage of instance and static
methods.
Concepts Covered: Instance Methods, Static Methods"""
class Calculator:
    def __init__(self,a,b):
        self.a = a 
        self.b = b
        
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a-self.b 
    @staticmethod
    def mul(x,y):
        return x*y
#instance method
calc = Calculator(7,4)
print(f"Addition:{calc.add()}")
print(f"Substraction:{calc.sub()}")
#static method
print(f"Multiplication:{Calculator.mul(2,3)}")
