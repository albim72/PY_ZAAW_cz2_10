class AttributeVallidator(type):
    def __new__(cls,name,bases,attrs):
        print(attrs.items())

        for attr_name,attr_value in attrs.items():
            if not attr_name.startswith("__"):
                if not isinstance(attr_value,int):
                    raise TypeError(f"{attr_name} musi byc w typie int")


        return super().__new__(cls,name,bases,attrs)

try:
    class SpecClass(metaclass=AttributeVallidator):
        x = 78
        y = 535
        z = 645
except TypeError as e:
    print(e)
