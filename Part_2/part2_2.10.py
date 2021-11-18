# Пространство имен класса

class DepartamentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info2(self):
        print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    # @property
    # def info_prop(self):
    #     print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    #
    # @classmethod
    # def info_class(cls):
    #     print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)
    #
    #
    # @staticmethod
    # def info_static():
    #     print('Info static')
    #     print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    def hiring_pyt_dev(self):
        DepartamentIT.PYTHON_DEV +=1 #так меняется атрибут класса DepartamentIT
        self.PYTHON_DEV +=1 #так создается копия атрибута класса DepartamentIT, и основное значение PYTHON_DEV
        # останется прежним (создаётся локальный атрибут внутри экземпляра класса)




    # def make_backend(self):
    #     print('Python and Go')
    #
    # def make_frontend(self):
    #     print("React")


it1 = DepartamentIT()
# it1.info()
# it1.info2()
# it1.info_prop
# it1.info_class()
# it1.info_static()
it1.info()
it1.hiring_pyt_dev()
it1.info()
