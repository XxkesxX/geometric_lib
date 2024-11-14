def area(a):
    '''Принимает сторону квадрата и возвращает его площадь'''

    if a < 0:
        raise ValueError("--Сторона квадрата не может быть отрицательной--")
    if type(a) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return a * a


def perimeter(a):
    '''Принимает сторону квадрата и возвращает его периметр'''

    if a < 0:
        raise ValueError("--Сторона квадрата не может быть отрицательной--")
    if type(a) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return 4 * a
