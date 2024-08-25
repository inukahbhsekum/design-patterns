import copy

class Prototype:

    def __init__(self):
        self._objects = dict()
    
    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def unregister_object(self, name):
        del self._objects[name]
    
    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
    

class Car:
    def __init__(self):
        self.name = "Mustang"
        self.color = "Red"
        self.options = "Ex"
    
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
    

c = Car()
print(c)
prototype = Prototype()
prototype.register_object('Mustang', c)
c1 = prototype.clone('Mustang', color='Green', options="New one")
print(c1)