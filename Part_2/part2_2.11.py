# практикуемся с property
from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password  # был __password, но после появления settera, убираем __ тем самым сразу запускаем
        # функцию проверки def password, и в конце когда функция отработает, пароль устанавливается

    @property
    def password(self):
        print("getter")
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, new_password):
        print("setter new password")
        if not isinstance(new_password, str):
            raise TypeError("Пароль должен быть строкой")
        if len(new_password) < 4:
            raise ValueError("Ваш пароль слишком короткий,минимум 6 символов")
        if len(new_password) > 12:
            raise ValueError("Ваш пароль слишком длинный,максимум 12 символов")
        if not User.is_include_number(new_password):
            raise ValueError("пароль должен содержать хотя бы 1 цифру")
        self.__password = new_password


q = User("Ivan", 12345)
