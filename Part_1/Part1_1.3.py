# #Атрибуты класса
# class Person:
#     name = "Ivan"
#     age = 30
#
#
# # pprint.pprint((Person.__dict__))
# #print(Person.name)
#
# Person.name = 'Misha'
# print(Person.name)


# class Hero:
#     live = 10
#     damage = 0
#
#
# print(setattr(Hero,'damage', 100))
# Hero.damage = 1001
# print(Hero.damage)
# print(Hero.x)

# Атрибуты экземляра класса
# class Car:
#     model = 'BMW'
#     engine = 1.6
#
#     @staticmethod
#     def drive():
#         print("Let's go")
#
# Car.drive()
#
# getattr(Car,"drive")()
# car_b = Car()
# car_b.drive()

# class Lion:
#
#     def roar(self):
#         print("Rrrrrrr!!!")
#
#
# simba = Lion()
# simba.roar() # печатает Rrrrrrr!!!



# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display()  # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display()  # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display()  # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"