"""Create a class Rectangle with attributes width and height. Implement the __init__ method to initialize
these attributes. Override the __str__ and __repr__ methods to provide a string representation of the
rectangle. Create an instance and print it to see the custom string representation.
Concepts Covered: Magic Methods (__init__, __str__, __repr__) """
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Width of rectangle is {self.width} and height is {self.height}"

    def __repr__(self):
        return f"rectangle{self.width},{self.height}"
    
r = Rectangle(12,20)
print(r)
print(repr(r))
          
