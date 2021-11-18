# Property. Getter-метод и setter-метод

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):  # Только Получает баланс
        print("get balance")#показатель того что выводит этот метод класса
        return self.__balance

    def set_balance(self, value):  # Перезаписывает в баланс тем значением которое вошло в value с проверкой на число
        print("set balance")#показатель того что выводит этот метод класса
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        self.__balance = value

    def delete_balance(self):
        print("delete balance")#показатель того что выводит этот метод класса
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)#Метод property

#m.balance - Выводит баланс пользователя
#m.balance = 600  - Устанавливает пользователю новое значение баланса(Только инт и флоат)
#del m.balance - Удаляет баланс у необходимого пользователя
