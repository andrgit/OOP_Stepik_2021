# # Практика. Класс Point(x,y)
# from math import sqrt
#
#
# class Point:
#     list_points = []
#
#     def __init__(self, coord_x=0, coord_y=0):
#         self.move_to(coord_x,coord_y)
#         Point.list_points.append(self)
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def go_home(self):
#         self.move_to(0,0)#переписываются значения на 0
#
#     def print_point(self):
#         print(f"Точка с координаторами ({self.x},{self.y})")
#
#     def calc_distance(self,another_point):
#         if not isinstance(another_point,Point):
#             raise ValueError("Аргумент должен принадлежать классу")
#         return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)#формула получения числа пифагора
#
# p7 = Point(6,0)
# p8 = Point(0,8)
# print(p7.calc_distance(p8))


# class Dog:
#     """Класс инициализирующий собаку"""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         """Метод, который возвращает строку в виде '<name> is <age> years old'
#                 """
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self,sound):
#         """Метод принимающий один аргумент,который возвращает строку вида '<name> says <sound>'
#                 """
#         #self.sound = sound
#         return f"{self.name} says {sound}"
#
#
# jack = Dog("Jack",3)
# print(jack.description())
# print(jack.speak("Woof Woof"))

class Stack:

    def __init__(self):  # Создаёт пустой стэк - *
        self.values = []

    def push(self, item):  # Вызываем метод и передаем в стэк значение - *
        self.values.append(item)

    def pop(self):  # Удаление верхнего элемента из стэка - *-
        if not self.values:
            print("Empty Stack")
        else:
            return self.values.pop()

    def peek(self):  # возвращает верхний элемент стека, но не удаляет его.
        if not self.values:
            print("Empty Stack")
        else:
            return self.values[-1]

    def is_empty(self):  # Проверяет стек на пустоту. Возврат булеан
        if len(self.values) == 0:
            return True
        else:
            return False

    def size(self):  # Возвращает кол-во элементов в стеке. Целое число
        return len(self.values)


s = Stack()  # +
s.peek()  # распечатает 'Empty Stack' +
print(s.is_empty())  # распечатает True+
s.push('cat')  # кладем элемент 'cat' на вершину стека+
s.push('dog')  # кладем элемент 'dog' на вершину стека+
print(s.peek())  # распечатает 'dog'- напечатало ['cat']
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3 +
print(s.is_empty())  # распечатает False+
s.push(777)  # кладем элемент 777 на вершину стека +
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его +
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его+
print(s.size())  # распечатает 2+
