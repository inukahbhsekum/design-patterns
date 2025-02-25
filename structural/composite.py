class Component(object):
    """Abstract class"""
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    """Concrete class"""
    def __init__(self, *args, **kwargs):
        Component.__init__(self,*args,**kwargs)
        self.name = args[0]

    def component_function(self):
        print("{}".format(self.name))


class Composite(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)
    
    def component_function(self):
        print("{}".format(self.name))
        for child in self.children:
            child.component_function()


sub1 = Composite("submenu1")
sub11 = Child("submenu11")
sub12 = Child("submenu12")
sub1.append_child(sub11)
sub1.append_child(sub12)
top = Composite("top_menu")
sub2 = Child("submenu2")
top.append_child(sub1)
top.append_child(sub2)
top.component_function()