
from datetime import datetime,time
class Person:
    def __init__(self,name,year,city):
        self._name = name
        self._year = year
        self.city = city
        self.__desc = "uczestnik konkursu"
        self.howmany = 9

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name

    @property
    def age(self):
        value = datetime.now().year - self._year
        age_ = value + self.howmany
        return value, age_

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self,times):
        newyear, month = times
        self._year = newyear + month/12

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self,newcity):
        self._city = newcity




p = Person("Jacek",1973,"Kraków")
print(p.name)
print(p.city)
print(p._year)
p.name = "Janek"
print(p.name)
# print(p.__desc)
print(p.age)

print(p.year)
p.year=1976,8
print(p.year)
print(p._city)


