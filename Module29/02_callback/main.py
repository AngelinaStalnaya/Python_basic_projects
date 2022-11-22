from typing import Callable, Any


app = dict()


def callback(route: str) -> Callable:
    def inner_wrapper(func: Callable) -> Callable:
        app[route] = func

        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)
        return wrapper
    return inner_wrapper


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')

if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')


@callback('C://')
def my_func():
    print('Другая функция')
    return 'OKOK'

print()

route2 = app.get('C:')

if route2:
    response2 = route()
    print('Ответ:', response2)
else:
    print('Такого пути нет')