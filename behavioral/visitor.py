class House(object):
    def accept(self, visitor):
        visitor.visit(self)
    
    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self):
        return self.__class__.__name__
    

class Visitor(object):
    ## abstract class
    def __str__(self):
        return self.__class__.__name__
    

class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


hvac_specialist_1 = HvacSpecialist()
electrician_1 = Electrician()
house_1 = House()
house_1.accept(hvac_specialist_1)
house_1.accept(electrician_1)