import functools
from collections.abc import Callable
from typing import Any


def decorator_with_args_for_any_decorator(decorator: Callable = None) -> Callable:
    """
    Декоратор, с возможностью принятия другим декоратором аргументов
    :param decorator: любой другой декоратор
    :param args: любые арги
    :param kwargs: любые кварги
    :return: вложенный декоратор
    """
    @functools.wraps(decorator)
    def wrapper(*args, **kwargs) -> Any:
        print('Переданные арги и кварги в декоратор: ', args, kwargs)
        return decorator
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return func(*args, **kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
