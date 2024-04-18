from abc import ABC, abstractmethod
from typing import Any
import math


class Figure(ABC):
    """Абстрактный базовый класс 2D Фигуры
    абстрактные методы: find_perimeter (нахождения периметра фигуры) и
    find_square (нахождения площади фигуры) переопределяются в дочерних классах"""

    def __init__(self, size: int) -> None:
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: int):
        if size > 0:
            self._size = size

    @abstractmethod
    def find_perimeter(self):
        pass

    @abstractmethod
    def find_square(self):
        pass


class Triangle(Figure):
    """Дочерний класс 2D фигуры Треугольник, родительский класс Figure"""

    def __init__(self, size: int, height: int) -> None:
        super().__init__(size=size)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: int):
        if height > 0:
            self._height = height

    def find_perimeter(self) -> [int, float]:
        return self._size + 2 * math.sqrt((self._size / 2) ** 2 + self._height ** 2)

    def find_square(self) -> [int, float]:
        return self._size * self._height / 2


class Square(Figure):
    """Дочерний класс 2D фигуры Квадрат, родительский класс Figure"""

    def find_perimeter(self) -> int:
        return self._size * 4

    def find_square(self) -> int:
        return self._size ** 2


class Pyramid(Triangle, Square):
    """Класс 3D фигуры Пирамида, родительские классы Triangle и Square"""

    def __init__(self, size: int, height: int) -> None:
        super().__init__(size=size, height=height)
        self.surface = [Triangle, Triangle, Triangle, Triangle, Square]

    def find_all_square(self) -> [int, float]:
        res = sum(item.find_square(self) for item in self.surface)
        return res


class Cube(Square):
    """Класс 3D фигуры Куб, родительский класс Square"""

    def __init__(self, size: int) -> None:
        super().__init__(size=size)
        self.surface = [Square, Square, Square, Square, Square, Square]

    def find_all_square(self) -> [int, float]:
        res = sum(item.find_square(self) for item in self.surface)
        return res


triangle = Triangle(size=3, height=6)
print(f'Периметр треугольника: {triangle.find_perimeter()}')
print(f'Площадь поверхности треугольника: {triangle.find_square()}')
square = Square(size=7)
print(f'Периметр квадрата: {square.find_perimeter()}')
print(f'Площадь поверхности квадрата: {square.find_square()}')
pyramid = Pyramid(size=5, height=4)
cube = Cube(size=9)
print(f'Площадь поверхности пирамиды: {pyramid.find_all_square()}')
print(f'Площадь поверхности куба: {cube.find_all_square()}')
