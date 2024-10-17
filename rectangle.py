def area(a, b): 
    '''Принимает две стороны
       прямоугольника и возвращает его площадь'''
    return a * b 

def perimeter(a, b):
    '''Принимает две стороны
       прямоугольника и возвращает его периметр'''
    return 2 * (a + b)


print(f"При a = 2, b = 7 S = {area(2, 7)}")
print(f"При a = 5, b = 4 P = {perimeter(5, 4)}")
