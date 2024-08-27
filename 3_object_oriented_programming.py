"""3_object_oriented_programming.py

We will study this chapter using python 2 syntax as SIRP automates scripts using Python2 however all of that code will be commented.
In order to run python2, we will have to create a virtual enviornment first but i don't want to dive into that right now therefore 
just use an online compiler to test the code in python2.

Before moving forward, i would appreciate you read this article to understand the core differences
between Python2 and Python3

Articile link: 
https://www.datacamp.com/blog/python-2-vs-3-everything-you-need-to-know

What to cover:

3.1 Classes and Objects
3.2 Inheritance
3.3 Polymorphism
3.4 Abstraction
3.5 Practice Quesitions
"""


#3.1 Classes and Objects
#3.1.1 Introduction to classes and objects

#Class is a blueprint for creating objects(a data structure), defining a set of attributes 
#and methods that characterize any object of that class.

#Objects are instances of a class, its a specific realization of a class with actual data.

#creating a class
"""class ClassName:
    # Constructor
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    # Method
    def method_name(self):
        return self.attribute1

#creating an object
my_object = ClassName("value1", "value2")
"""
#Example in Python2:

"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return "%s says Woof!" % self.name

dog1 = Dog("Buddy", "Golden Retriever")
print dog1.bark()  # Output: Buddy says Woof!
"""

#3.1.2 Instance attributes and methods

#Instance Attributes: Attributes that are specific to each object. They are
#defined in the __init__ method and accessed using self.

#Instance Methods: Functions defined inside a class that operate on instances
#of the class. These methods take self as their first parameter.

#Example in Python2:
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return "%s %s is starting." % (self.make, self.model)

# Creating an object
car1 = Car("Toyota", "Camry", 2020)
print car1.start()  # Output: Toyota Camry is starting.
"""
#3.1.3 class attribute and methods
#Class Attributes: Attributes that are shared across all instances of a class.
#They are defined directly inside the class but outside any method.

#Class Methods: Methods that operate on the class itself rather than on instances
#of the class. They are defined with the @classmethod decorator and take cls as their
#first parameter.

"""class Animal:
    species = "Mammal"  # Class Attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def general_info(cls):
        return "All animals of this class are %s." % cls.species

# Creating an object
animal1 = Animal("Elephant")
print animal1.general_info()  # Output: All animals of this class are Mammal.
"""

#3.1.4 Static Methods
#Static Methods: Methods that do not operate on the class or its instances.
#They are defined with the @staticmethod decorator and do not take self or
#cls as their first parameter.

"""class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method
result = MathOperations.add(5, 7)
print result  # Output: 12

"""

#3.2 Inheritance
#3.1.2 Understanding Inheritance
#A mechanism that allows a new class to inherit attributes and methods from 
#an existing class. The new class is called a child class or subclass, and 
#the existing class is the parent class or superclass.

#basix structure
"""class ParentClass:
    # Parent class code here

class ChildClass(ParentClass):
    # Child class code here
"""

#Exaample in python2
"""
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        return "The vehicle is starting."

class Car(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model)  # Using the parent class's __init__ method
        self.year = year

    def start(self):
        return "The %s %s %s is starting." % (self.year, self.make, self.model)

# Creating an object of the Car class
car1 = Car("Toyota", "Camry", 2020)
print car1.start()  # Output: The 2020 Toyota Camry is starting.

"""
#3.2.2 Method overriding
#The process of redefining a method in the child class that already exists in the parent class.

"""
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

dog = Dog()
print dog.sound()  # Output: Woof!

"""

#3.2.3 Multiple Inheritance
"""
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    def method_c(self):
        return "Method C"

c = C()
print c.method_a()  # Output: Method A
print c.method_b()  # Output: Method B
print c.method_c()  # Output: Method C
"""

#3.3 Polymorphism 
#3.3.1 Understanding Polymorphism
#The ability to use a common interface for multiple
#forms (data types). In Python, polymorphism allows 
#functions or methods to work on different types of objects.

"""
class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound(self):
        return "Woof"

def make_sound(animal):
    return animal.sound()

bird = Bird()
dog = Dog()

print make_sound(bird)  # Output: Chirp
print make_sound(dog)   # Output: Woof
"""
#3.3.2 Polymorphism with Inheritance

"""
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print shape.area()  # Output: 78.5, 16

"""

#3.4 Abstraction
#3.4.1 Understanding Abstraction
#Abstraction: Abstraction is the concept of hiding the complex implementation details and showing 
#only the essential features of an object. In Python, abstraction can be achieved using abstract 
#classes and abstract methods.

#An abstract class cannot be instantiated and usually contains one or more abstract methods that
#must be implemented by any subclass.

"""
import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta  # Mark this as an abstract class

    @abc.abstractmethod
    def area(self):
        #Calculate the area of the shape.
        return

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Abstract class cannot be instantiated
# shape = Shape()  # This will raise an error

# But we can instantiate its subclasses
rectangle = Rectangle(10, 20)
print rectangle.area()  # Output: 200

circle = Circle(5)
print circle.area()  # Output: 78.5

"""

#3.4.2 When to Use Abstraction
"""Abstract Shape Class:

Simplifying Complex Systems: Abstraction allows you to work with complex systems by simplifying and 
managing complexity through high-level interfaces.

Enforcing Method Implementation: It ensures that a method is implemented by all subclasses, providing 
a consistent interface.
"""

#3.5 Practice Quesitons:

#3.5.1 Create a Temperature class with a static method to convert Celsius to Fahrenheit and another 
#to convert Fahrenheit to Celsius.

#3.5.2 Implement a polymorphic system where different payment methods (e.g., CreditCard, PayPal, Bitcoin)
#are handled by a single process_payment() function.

#3.5.3 Create two parent classes, FlyingAnimal and SwimmingAnimal, with methods fly() and swim() respectively.
#Then, create a child class Duck that inherits from both and implements both methods.



