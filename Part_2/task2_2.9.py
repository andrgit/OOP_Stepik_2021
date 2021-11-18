class Example:
    def hello():
         print('Hello')

    def instance_hello(self):
        print(f'instance_hello {self}')

    @staticmethod
    def static_hello():
        print('static hello')


    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')