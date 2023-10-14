"""
Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes.

"""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  # Create a Plane class

for x in (car1, boat1, plane1):
    x.move()

"""
Inheritance Class Polymorphism
What about classes with child classes with the same name? Can we use polymorphism there?

Yes. If we use the example above and make a parent class called Vehicle, and make Car, 
Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

Child classes inherits the properties and methods from the parent class.

In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

Because of polymorphism we can execute the same method for all classes.


"""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

"""
inheritance example

"""


class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
