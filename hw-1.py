class Cow():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
     print(f"{self.name}: mu,mu,mu ,  ей  - {self.age} лет")



class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def voice(self):
        print(f'{self.name} gav, gav gav, ей - {self.age}лет')


class Bear():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def voice(self):
        print(f'{self.name} aр, ей - {self.age}лет')


class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        print(f'{self.name}  Мяу, ей - {self.age}лет')


cow = Cow('Luba', 7)
cow.voice()
Dog = Dog('Sharic', 5)
Dog.voice()
bear = Bear('adel',14)
bear.voice()
cat = Cat ('ali',9)
cat.voice()