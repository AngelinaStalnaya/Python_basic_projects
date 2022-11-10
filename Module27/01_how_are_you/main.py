import functools
from typing import Callable, Any


def how_are_you(function: Callable) -> Callable:
    """
    Декоратор - жалобщик. Интересуется у пользователя о состоянии дел,
    а после жалуется, что у него всё плохо.
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        answer = input('Как дела? ').lower()
        print(f'{"А у меня не очень!" if answer == "хорошо" or answer == "ok" else "И у меня не очень!"} '
              f'Ладно, держи свою функцию.')
        result = function(*args, **kwargs)
        return result
    return wrapper


@how_are_you
def test() -> None:
    """
    Какая-то функция пользователя
    :return: None
    """
    print('<Тут что-то происходит...>')


test()
# print(test.__name__)
# print(test.__doc__)
