"""Q1	"Define a class named Car with attributes make, model, and year. Create a constructor to initialize these attributes.
Create an instance of Car and display its attributes.
Concepts Covered: Class, Object, Constructor, Instance Variables"""
class Car():
    def __init__(self,make,model,year):     #constructor
        self.make = make
        self.model = model
        self.year = year
        
achine = Car('Mahindra','3XO','2024') #instance of car
#display its attributes
print(f"Make:{machine.make}\nModel:{machine.model} \nYear:{machine.year}")
	
