

class MyMath:
    """
    Класс, содержащий математические формулы для вычисления
    Методы:
    circle_len - возвращает вычисление длины окружности
    circle_sq - возвращает вычисление площади окружности
    circle_sphere - возвращает вычисление площади поверхности сферы
    cube_volume - возвращает вычисление объёма куба
    cube_square - возвращает вычисление площади поверхности куба
    """
    pi = 3.14159265359

    @classmethod
    def circle_len(cls, radius) -> float:
        return 2 * cls.pi * radius

    @classmethod
    def circle_sq(cls, radius) -> float:
        return cls.pi * radius ** 2

    @classmethod
    def circle_sphere(cls, radius) -> float:
        return 4 * cls.pi * radius ** 2

    @classmethod
    def cube_volume(cls, size) -> int:
        return size ** 3

    @classmethod
    def cube_square(cls, size) -> int:
        return 6 * size ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.circle_sphere(radius=3)
res_4 = MyMath.cube_volume(size=9)
res_5 = MyMath.cube_square(size=7)
print('Результат: ')
print(f'Длина окружности: {res_1}')
print(f'Площадь окружности: {res_2}')
print(f'Площадь поверхности сферы: {res_3}')
print(f'Объём куба: {res_4}')
print(f'Площадь поверхности куба: {res_5}')
