import functools
from typing import Callable, Any
import datetime


def logging(function: Callable) -> Callable:
    """
    Декоратор, логирующий функции. При наличии ошибки - запись даты, времени и названия ошибки.
     В случае отсутствия ошибки - вывод наименования и документации функции
    :param function: любая функция
    :return: Наименование и документация функции
    """
    @functools.wraps(function)
    def wrapping() -> Any:
        try:
            print(function.__name__)
            print(function.__doc__)
        except Exception as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as file_to:
                file_to.write(f'{datetime.datetime.now()} с функцией {function.__name__} возникла ошибка {exc}\n')
    return wrapping


@logging
def func_1() -> None:
    """
    Функция нахождения суммы чисел в диапазоне от 1 до 10, возведенных в 3ю степень
    :return: None
    """
    print(sum(x ** 3 for x in range(1, 11)))


@logging
def func_2() -> int:
    """
    Функция нахождения суммы чисел в диапазоне от 1 до 10, возведенных в 5ю степень
    :return: сумма чисел от 1 до 15 с шагом 5 в 5й степени
    """
    return sum(x ** 5 for x in range(1, 16, 5))


func_1()
func_2()
