
class Counter:
    """Класс-декоратор, подчитывающий количество вызовов декорируемой функции"""

    def __init__(self,  func):
        self.counter = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f'Функция {self.func.__name__} вызвалась в {self.counter} раз')
        return self.func(*args, **kwargs)


@Counter
def my_func() -> str:
    """Функция возврата слова "Hello"."""
    return 'Hello'


@Counter
def my_func_2() -> None:
    """Функция вывода слова "Hi"."""
    print('Hi')


@Counter
def my_func_3() -> None:
    """Функция вывода слова "Bye"."""
    print('Bye')


my_func()
my_func_2()
my_func_3()
my_func()
my_func_2()
my_func()
