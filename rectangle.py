def area(a, b): 
    '''Принимает две стороны
       прямоугольника и возвращает его площадь'''

    if a < 0 or b < 0:
        raise ValueError("--Сторона прямоугольника не может быть отрицательной--")
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return a * b 

def perimeter(a, b):
    '''Принимает две стороны
       прямоугольника и возвращает его периметр'''

    if a < 0 or b < 0:
        raise ValueError("--Сторона прямоугольника не может быть отрицательной--")
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("--Введен неверный тип данных--")

    return 2 * (a + b)
