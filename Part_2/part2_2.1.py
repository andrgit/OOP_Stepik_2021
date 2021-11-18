# class Counter:
#
#     def start_from(self, value=0):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def display(self):
#         print(f"Текущее значение счетчика = {self.value}")
#
#     def reset(self):
#         self.value = 0
#
#
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"


class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, pifagor):
        if isinstance(pifagor, Point):
            return (((self.x - pifagor.x) ** 2 + (self.y - pifagor.y) ** 2) ** 0.5)
        else:
            print("Передана не точка")


p1 = Point()
p2 = Point()

p1.set_coordinates(1, 2)  # передаётся в p1 значение x=1, y=2
p2.set_coordinates(4, 6)  # передаётся в p2 значение x=4, y=6

d = p1.get_distance(p2)  # вернёт 5.0
print(d)  # распечатает 5.0
p1.get_distance(10)  # Распечатает "Передана не точка"
