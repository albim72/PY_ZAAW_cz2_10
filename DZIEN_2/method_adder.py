class MethodAdder(type):
    def __new__(cls,name,bases,attrs):
        attrs['print_class_name'] = lambda self: print(f"jestem klasą: {self.__class__.__name__}")
        attrs['class_name'] = property(lambda self:self.__class__.__qualname__)
        return super().__new__(cls,name,bases,attrs)

class MojaKlasa(metaclass=MethodAdder):
    @property
    def class_name(self):
        return 432534543

class Druga(MojaKlasa):
    @property
    def class_name(self):
        return True

obj = MojaKlasa()
obj.print_class_name()
print(obj.class_name)

ob2 = Druga()
ob2.print_class_name()
print(ob2.class_name)
