""" Define a class Person with a class variable population_count. Implement an __init__ method to
initialize a person’s name. Add a class method increment_population to increase population_count
whenever a new person is created. Demonstrate the usage of the class method by creating multiple
instances of Person.
Concepts Covered: Class Method, Class Variables """
class Person:
    population_count = 0
    def __init__(self,name):
        self.name = name
        Person.increament_population()
    @classmethod
    def increament_population(cls):
        cls.population_count +=1

#creating multiple instances of person
p1 = Person("OM")
p2 = Person("Ritesh")
p3 = Person("Rohit")       

print(f"Population Count is {Person.population_count}")
