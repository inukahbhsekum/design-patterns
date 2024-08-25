class Director():
    """Director"""
    
    def __init__(self, builder):
        self._builder = builder


    def construct_car(self):
        """Calls for constructing new car by calling concrete builder functions"""
        
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    
    def get_car(self):
        """Returns the new car"""
        
        return self._builder.car


class AbstractBuilder():

    def __init__(self):
        self.car = None
    
    def create_new_car(self):
        self.car = Car()


class GWagonBuilder(AbstractBuilder):

    def add_model(self):
        self.car.model = "G-wagon builder"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class MustangBuilder(AbstractBuilder):

    def add_model(self):
        self.car.model = "Mustang builder"

    def add_tires(self):
        self.car.tires = "Offroad tires"

    def add_engine(self):
        self.car.engine = "Battery powered engine"


class Car:

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


builder = GWagonBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)

builder = MustangBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)