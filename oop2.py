# INHERITANCE
"""
= inheritance allows a class (class / subclass) to inherite attributes and methods from 
    another class (parent / superclass)
= This promotes code reuse and establishedf a hierachial relationship
"""

class Parent:
    pass
class Child(Parent):
    pass

"""
= The child inherits all methods and attributes from the parent but can override or extend them 

"""

# PORLYMORPHISM
"""
= Porlymorphism (many forms ) allows objects of different classes to be treated as instances of the same class through a common 
    parent class
= Its often achieved by overriding methods in the child classes, so each class can impliment the same 
    method differently
 ***
 = Child classes override parents methods 
 = You  can call the same method on different objects and python executes the appropriate version
"""

# ENCAPSULATION

"""
= Encapsulation bundles data (attributes) and methods within a class and controls access to them 
= It hides internal details and protects data from inintended modifications using private attributes
*** how it works: 
        = Public attributes/ methods : they are accessible everywhere
        = Protected attributes/methods : indicated by a single underscore (e.g self._name) a convention
          for dont touch this unless you're a subclass
        = Private attributes/ methods : indicated by double underscore (e.g self._name) which triggers
          name mangling to prevent direct access outside the class
= Use getters and setters to access of modify attributes safely 
"""
# ABSTRACTION
"""
= Abstraction hides complex implimenation details and exposes only the essential fetures to the user 
= It's achieved using abstract classes or methids that define what a class sjould do whithout specifying 
    how
***how it works: 
        = Use abc module to create abstract base classes (ABCs)
        = Define abstract methods with @abstractmethods that child must implement
        = You can't instantiate an abstract class directly
"""

