import math


def area(r):
    '''Принимает радиус окружности и возвращает её площадь'''

    if type(r) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")
    if r < 0:
        raise ValueError("--Радиус не может быть отрицательным--")

    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус окружности и возвращает его периметр'''

    if type(r) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")
    if r < 0:
        raise ValueError("--Радиус не может быть отрицательным--")

    return 2 * math.pi * r
