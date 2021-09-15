import math
import random
from typing import Any


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int and denom != 0
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        return Fraction((self.num * other.denom + other.num * self.denom), (self.denom * other.denom))

    def __sub__(self, other):
        return Fraction((self.num * other.denom - other.num * self.denom), (self.denom * other.denom))

    def __float__(self):
        return self.num / self.denom

    def __int__(self):
        return int(self.num / self.denom)

    def inverse(self):
        return Fraction(self.denom, self.num)


class Car(object):
    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""

    def paint(self, color):
        self.color = color

    def __eq__(self, other):
        if self.wheels == other.wheels and self.doors == other.doors and self.color == other.color:
            return True
        else:
            return False


# c = Coordinate(3, 4)
# c1 = Coordinate(6, 8)
# origin = Coordinate(0, 0)
# print(c.distance(c1))
# print(Coordinate.distance(c, c1))
# print(c)
# print(type(c))
# print(isinstance(c, Coordinate))

# f = Fraction(3, 4)
# f1 = Fraction(4, 3)
# print(f)
# print(f+f1)
# print(f-f1)
# print(float(f))
# print(f.inverse())
# print(int(f1))


# car1 = Car(4, 2)
# car2 = Car(4, 2)
# car3 = Car(4, 2)
# car2.paint("red")
#
# print(car1 == car2)
# print(car1 == car3)


class Animal(object):
    def __init__(self, age, name=None):
        assert type(age) == int and (type(name) == str or name is None) and age != None
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, newname=""):
        self.name = newname

    def set_age(self, newage):
        self.age = newage

    def __str__(self):
        return "Animal: " + str(self.name) + "\nAge: " + str(self.age)


a1 = Animal(7, "Dog")


# a1.identity = "Mickey"
# print(a1)
# print(a1.identity)
# a = Animal(5)
# a.set_name("Cat")
# print(a)


class Cat(Animal):
    def speak(self):
        print("Meow")

    def __str__(self):
        return "Cat:\n\tName:" + str(self.name) + "\n\tAge:" + str(self.age)


# c = Cat(7, "Meena")
# c.speak()
# print(c)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        self.friends.append(fname)

    def speak(self):
        print("Hello, I am", self.name)

    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")

    def __str__(self):
        return "Person:\n\tName:" + str(self.name) + "\n\tAge:" + str(self.age)


# p = Person("Kumaran", 21)
# p1 = Person("James", 25)
# print(p)
# print(p1)
# p.age_diff(p1)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if 0 <= r <= 0.25:
            print("I have homework")
        elif 0.25 < r <= 0.5:
            print("I need to eat")
        elif 0.5 < r <= 0.75:
            print("I need sleep")
        else:
            print("I am watching TV")

    def __str__(self):
        return "Student:\n\tName:" + str(self.name) + "\n\tAge:" \
               + str(self.age) + "\n\tMajor:" + str(self.major)


# s = Student("Snake", 20, "CSE")
# print(s)
# s.speak()


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, name, parent1=None, parent2=None):
        Animal.__init__(self, age, name)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return str(self.parent1)

    def get_parent2(self):
        return str(self.parent2)

    def __add__(self, other):
        return Rabbit(0, self.name + other.name, self, other)

    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and \
                       self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent2.rid and \
                           self.parent2.rid == other.parent1.rid
        return parents_same or parents_opposite

    def __str__(self):
        return "Rabbit:\n\tName:" + str(self.name) + "\n\tAge:" + str(self.age) + "\n\tParent1:" + str(self.parent1) \
               + "\n\tParent2:" + str(self.parent2) + "\n\tRabbitID:" + str(self.rid)


r = Rabbit(7, "Mosakutti")
# print(r)
r1 = Rabbit(6, "Muyalaamai")

r4 = r + r1
r5 = r1 + r
print(r4)
print(r4 == r5)
