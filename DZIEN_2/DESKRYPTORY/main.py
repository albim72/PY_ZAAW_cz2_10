from desc1 import Person
from desc2 import MClass
from desc3 import MojLog

#przykład desc1
print("przykład desc1")

try:
    p = Person("Jan",56)
    print(p.name)
    print(p.age)

    p.age = "osiem"
    print(p.age)

except TypeError as tp:
    print(tp)

#przyklad desc2
print("przykład desc2")
try:
    ob = MClass()
    print(ob.constant)
    ob.constant = 900

except AttributeError as a:
    print(a)

#przyklad desc3
print("przykład desc3")
try:
    print("_"*50)
    trzeci = MojLog()
    trzeci.x = 10
    print(trzeci.x)

    print("_" * 50)
    del trzeci.x
    print(trzeci.x)

    print("_" * 50)
    trzeci.y = "ładna jesień"
    print(trzeci.y)

    print("_" * 50)
    del trzeci.y
    print(trzeci.y)

except Exception as exc:
    print(exc)
