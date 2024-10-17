import math


def area(r):
    '''Принимает радиус окружности и возвращает её площадь'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус окружности и возвращает его периметр'''
    return 2 * math.pi * r

print(f"При r = 3 S = {area(3)}")
print(f"При r = 5 P = {perimeter(5)}")
