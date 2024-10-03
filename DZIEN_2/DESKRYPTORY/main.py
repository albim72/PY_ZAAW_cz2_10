from desc1 import Person
from desc2 import MClass

#przykład desc1

try:
    p = Person("Jan",56)
    print(p.name)
    print(p.age)

    p.age = "osiem"
    print(p.age)

except TypeError as tp:
    print(tp)

#przyklad desc2

try:
    ob = MClass()
    print(ob.constant)
    ob.constant = 900

except AttributeError as a:
    print(a)
