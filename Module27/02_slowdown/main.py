import functools
from typing import Callable, Any
import time


def add_seconds(function: Callable) -> Callable:
    """
    Декоратор, добавляющий 3 секунды перед выполнением основной функции
    :param function: любая функция, требующая "замедления"
    :return: функцию, выполнение которой отложено на 3 сек
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        time.sleep(3.0)
        result = function(*args, **kwargs)
        end_time = time.time()
        function_time = end_time - start_time
        print(f'Стартовое время: {start_time}')
        print(f'Время окончания выполнения функции: {end_time}')
        print(f'Время выполнения функции c учетом "отложения": {function_time}')
        return result
    return wrapper


@add_seconds
def my_func() -> None:
    return sum(x ** 5 for x in range(10))


my_func()