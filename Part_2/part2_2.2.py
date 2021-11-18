# class Cat:
#
#     def __init__(self, name, breed='siam', age=1, color='black'):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.color = color
#
# jerry = Cat("Jerry")
# print(jerry.age)
#
#
# tom = Cat("Tom","Maikun",10,"white")
# print(tom.age)

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f"{brand} {model}"
#
#
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"
#
# laptop1 = Laptop("Apple","MacBook Pro",100000)
# laptop2 = Laptop("Lenovo", "LS100", 555555)


# class SoccerPlayer:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics()  # выводит "Messi Leo - голы: 700, передачи: 500"
#
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics()  # выводит "Kokorin Alex - голы: 1, передачи: 0"
#Выводит 1 гол и 0 переда потому что гол -score() мы инициализируем, и он присваивает 1. А make_assist()
# не инициализируется по этому берется значение 0 из конструктора __init__


# class Zebra:
#
#     def __init__(self, stripe="Полоска белая", counter=0):
#         self.stripe = stripe
#         self.counter = counter
#
#     def which_stripe(self):
#         if self.counter == 0:
#             print(self.stripe)
#             self.counter += 1
#         else:
#             print("Полоска черная")
#             self.counter = 0
#
#
# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"



class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"
 
    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult())