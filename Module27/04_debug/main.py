import functools
from typing import Callable, Any


def debug(function: Callable) -> Callable:
    """
    Декоратор, выводящий наименование, передаваемые параметры,
     значение и результат функции
    :param function: любая функция
    :return: входные и выходные параметры декорируемой функции
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        result = function(*args, **kwargs)
        str_args_and_kwargs = ''
        if args:
            for i in args:
                str_args_and_kwargs += repr(i) + ', '
        if kwargs:
            for j in kwargs:
                str_args_and_kwargs += f'{j}={repr(kwargs[j])}, '
        str_args_and_kwargs = str_args_and_kwargs[:-2]

        print(f"Вызывается {function.__name__}({str_args_and_kwargs})")
        print(f"'{function.__name__}' вернула значение {repr(result)}")
        if kwargs:
            print(f'Ого, {args[0] if len(kwargs)== 1 else kwargs["name"]}! Тебе уже {kwargs["age"]} лет, {"ты быстро растёшь" if kwargs["age"] < 20 else "ты вырос"}!\n')
        else:
            print(result + '\n')
        return
    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)