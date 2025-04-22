# OBJECT ORIENTED PROGRAMMING IN PYTHON
"""
=> oop is a programming paradigm that orginizes code around objects rather than functions or procedures
=> objects are instances of classes, which act as blueprints defining the properties (data) and behaviours
(functions/methods) of those objects.
=> oop models real world entities, making code more intutive and modular
"""
# CONCEPT OF OOP
"""
=> CLASES AND OBJECTS
                    * a class is a templated and an object is aan instance of that class
= encapsulation
        * the bundling of data and methods that operate on that data within a single unit (class)
        * restricts direct access to some components, which is a means of preventing unintended interference and misuse
= inheritance:
        * a mechanism where a new class can inherit attributes and methods from an existing class
        * promotes code reusability and establishes a relationship between classes
= polymorphism:
        * the ability to present the same interface for different data types
        * allows methods to do different things based on the object it is acting upon
= abstraction:
        * the concept of hiding the complex reality while exposing only the necessary parts
        * it helps to reduce programming complexity and effort
 """

# BENIFITS OF OOP
"""
# MODULARITY
 => code is organized into classes, making it easier to manage and update
 #REUSABILITY
 => inheritance and polymorphism allow code to be reused acress projects
 # SCALABILITY
 => OOP suits large, complex systems by breaking then into managable pieces
 # MAINTAINABILITY
 => encapsulation isolates, changes redusing bugs and simplfying degbugging
 # REAL-WORLD MODELLING
 => oop minics real-world realtionships, making systems intuative to design and understand

"""
# DEFINING CLASSES AND CREATING OBJECTS
"""
= A Class is created using the class keyword, and objects are created by instantiatingthe class
= You can create an object by calling the class as if it were a function
"""
class cat:
    def meow(self):
        print("Meow!")
#create object/instances
cat1 = cat()
cat2 = cat()
#Calling the meow method
cat1.meow() # Output: Meow!
cat2.meow() # Output: Meow!

"""
=> cat1 and cat2 are objects 
=> each objects can access the class methods independently
"""
#ATTRIBUTES AND METHODS WITHIN A CLASS
"""
= Attributes are variables that belong to a class
= Methods are functions that belong to a class
"""
#ATTRIBUTES
"""
a) Instances attributes: Unique to each object, defined using self in in thr _init_ method
b) Class attributes: Shared across all instances of the class, defined outside any methods
= the _init_ method is a special method that initializes the object's attributes when an object is created
"""
class Dog:
    #class attribute
    species = "German Shepherd"
    def _init_(self, name, age):
        #instance attributes
        self.name = name
        self.age = age
dog1 = Dog("Max", 5)
dog2 = Dog("Buddy", 3)

"""
=> species is a class attribute, same for all dogs
=> name and age are instance attributes, unique to each dog
"""
#METHODS
"""
= Methods are functions defined within a class that operate on the attributes of the class
= They are called using the dot notation on an object

TYPES OF METHODS:
1) Instance methods: Operate on instance attributes and can access class attributes
2) Class methods: Operate on class attributes and are defined using the @classmethod decorator
3) static methods: dont access object or class data (decorated with staticmethod)
"""
class Dog:
    species = "German Shepherd"
    def _init_(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def describe(self):
        print(f"{self.name} says Woof!")

    #class method
    @classmethod
    def get_species(cls):
        return cls.species

    #static method
    @staticmethod
    def info():
        print("Dogs are loyal animals.")