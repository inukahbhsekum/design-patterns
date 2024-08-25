class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"
    
    def __str__(self):
        return "Dog"
    

class Cat:
    """One of the objects to be returned"""

    def speak(self):
        return "Meow!"
    
    def __str__(self):
        return "Cat"


class CatFactory:
    """Concrete cat factory"""

    def get_pet(self):
        return Cat()
    
    def get_food(self):
        return "Cat food"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns the dog object"""

        return Dog()

    def get_food(self):
        """Return the dog food object"""
        
        return "Dog Food"


class PetStore:
    """Pet Store houses our pet factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our abstract factory"""

        self._pet_factory = pet_factory
    
    def show_pet(self):
        """Utility method for displaying the details of the returned object"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is : {}".format(pet))
        print("Our pet says hello by : {}".format(pet.speak()))
        print("It's food is : {}".format(pet_food))


# create a concrete factory
dog_factory = DogFactory()
cat_factory = CatFactory()

# create a pet_store , our abstract factory
shop1 = PetStore(dog_factory)
shop2 = PetStore(cat_factory)

# Invoke the utility method to show the details of our pet
shop1.show_pet()
shop2.show_pet()