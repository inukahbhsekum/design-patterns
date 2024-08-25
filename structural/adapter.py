class Korean:
    """Korean Speaker"""
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong"
    

class English:
    """English Speaker"""
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"


class Adapter:
    """This changes the generic method name to individualised method names"""
   
    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of the attributes"""
        return getattr(self._object, attr)

objects = []
korean = Korean()
british = English()
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
