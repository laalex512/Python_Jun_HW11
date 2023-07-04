'''Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений'''


class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, a: float, b: float = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self.a + self.b)

    def area(self):
        '''Метод расчета площади прямоугольника.'''
        return self.a * self.b

    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        sum = self.perimeter() + other.perimeter()
        aspect_side = min(self.a, self.b) / max(self.a, self.b)
        new_a = sum / 2 * aspect_side
        new_b = sum / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычетания двух прямоугольников.'''
        sub = abs(self.perimeter() - other.perimeter())
        aspect_side = min(self.a, self.b) / max(self.a, self.b)
        new_a = sub / 2 * aspect_side
        new_b = sub / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return f'Прямоугольник со сторонами: {self.a} и {self.b}'

    '''Для всех 6 операций сравнения достаточно определить только 3 метода, 
    противоположные python додумает сам)'''

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


if __name__ == '__main__':
    rect1 = Rectangle(2, 5)
    rect2 = Rectangle(5, 10)
    print(rect1)
    print(rect2)
    print(f'{rect1.perimeter()= } {rect1.area()= }')
    print(f'{rect2.perimeter()= } {rect2.area()= }')
    print('------------------------------------------------')
    rect_sum = rect1 + rect2
    print(rect_sum.a, rect_sum.b)
    rect_sub = rect1 - rect2
    print(rect_sub.a, rect_sub.b)
    print(rect_sub)
    print('------------------------------------------------')
    print(rect1 == rect2, rect1 != rect2)
    print(rect1 > rect2, rect1 <= rect2)
    print(rect1 < rect2, rect1 >= rect2)
