# MULTIPLY INHERITANCE AND METHOD RESOLUTION ORDER (MRO)
"""
= Multiple resolution allows a class to inherite for more that one parent class , combining their 
    attributes and methods 
= MRO determines thr order in ehich python searches for methods and attributes in a class hierachy
= Python uses theC3 linerlization algorithm to create a consistence, predictable order
***how it works:
        = When you class an method on an object, python looks for it in the class then follows the MRO
            to parent classes
        = The MRO is computed to avoid ambiguity ensuring each class is visited only once and respecting 
            the inheritance hierachy
"""
# PITFALLS AND THE PRACTICES
"""
= Diamond Problem: When two parents classes inherit from a common ancestor, leading to ambiguity in method resolution
= Complexitity: Multiple inheritance can introduce unexpected behavior and make the code harder to understand and maintain.
= Explicit super() usage: in complex hierachies, super() can behave unexpectedly unless you understand
    the MRO. Always check_MRO_when debugging
***WHY USE IT:
1. combaines functionality from multiplr classes (e.g A flying fish is both a flyer and a swimmer )
2. Useful in frameworks like Graphical user Interface (e.g widgit inheriting from multiple component classes)

"""
# PROPERTY DECORATORS FOE ENHANCED ENCAPSULATION
"""
= Property decoraters allow you to define methods that act like attributs, providing a clean way 
    to control accsses to instance data
= They enhance encapsulation by hiding details while offering attributes like syntax
***WHY USE IT :
= Controlled Access: They allow you to manage how attributes are set and retrieved, ensuring data integrity and validation.
"""