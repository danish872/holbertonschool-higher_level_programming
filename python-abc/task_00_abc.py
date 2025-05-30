from abc import ABC, abstractmethod
""" Import the necessary components from the abc module
    Define the abstract class Animal
"""
class Animal(ABC):
    """ Declare an abstract method named sound
        The abstract method doesn't have a body
    """
    @abstractmethod
    def sound(self):
        pass

""" Implement the Dog subclass"""
class Dog(Animal):
    """ Implement the sound method for Dog"""
    def sound(self):
        return "Bark"

""" Implement the Cat subclass"""
class Cat(Animal):
    """ Implement the sound method for Cat"""
    def sound(self):
        return "Meow"

if __name__ == "__main__":
    """ Create instances of Dog and Cat"""
    dog = Dog()
    cat = Cat()

    """ Print the sounds
        Output: Dog says: Bark
        Output: Cat says: Meow
    """
    print(f"{dog.sound()}")
    print(f"{cat.sound()}")

    """ Attempting to instantiate the abstract class Animal will raise a TypeError
        This will raise an error
        Output: Can't instantiate abstract class Animal with abstract method sound
    """
    try:
        animal = Animal()
    except TypeError as e:
        print(e)
