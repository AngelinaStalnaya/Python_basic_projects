import functools
from collections.abc import Callable


def check_permission(name: str, _func: Callable = None):
    def check_name(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if name == user_permissions[0]:
                    func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapper
    if _func is None:
        return check_name
    return check_name(_func)


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


@check_permission('admin')
def add_page():
    print('Добавляем страницу сайта')


delete_site()
add_comment()
add_page()