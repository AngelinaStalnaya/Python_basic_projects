from typing import Any
from collections.abc import Callable
import functools
import time
from datetime import datetime


def log_methods(date_format: str) -> Callable:
    def wrapper(cls) -> Callable:
        for method in dir(cls):
            if method.startswith("__") is False:
                current_method = getattr(cls, method)
                decorated_method = decorator(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls
    return wrapper


def decorator(cls, func: Callable, date_format) -> Callable:
    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> Any:
        new_format = date_format
        for sym in new_format:
            if sym.isalpha():
                new_format = new_format.replace(sym, f'%{sym}')
        start = time.time()
        print(f'- Запускается "{cls.__name__}.{func.__name__}". '
              f'Дата и время запуска: {datetime.now().strftime(new_format)}')
        result = func(*args, **kwargs)
        print(f'Тут метод {func.__name__} {"у наследника" if cls.__name__ == "B" else ""}')
        print(f'- Завершение "{cls.__name__}.{func.__name__}", время работы = {round(time.time() - start, 3)}s')
        return result
    return wrapper


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

