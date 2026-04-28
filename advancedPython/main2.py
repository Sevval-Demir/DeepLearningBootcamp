# section 2 : property decorators
# data validation, private/public (encapsulation)

print("=" * 60)
print("section 2 : property decorators")
print("=" * 60)


class Person:

    def __init__(self, name, age):
        self.__name = name  # __ konulduğunda private oluyor, dışarıdan erişilemez
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "Ela":
            print("Ela not accepted")
        else:
            self.__name = value

    @name.deleter
    def name(self):
        self.__name = None

    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            print("Name must be a string")
        if len(value)< 2:
            raise ValueError("Name must be at least 2 characters long")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if not isinstance(value, int):
            print("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be a positive integer")
        self.__age = value


sevval = Person("sevval", 21)
print(sevval.name)
sevval.name = "Sevval Demir"
print(sevval.name)
del sevval.name
print(sevval.name)
sevval.age=21
print(sevval.age)
