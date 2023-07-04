'''Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''

from datetime import datetime


class MyString(str):
    """Класс MyString - расширенный класс str, содержащий дополнительные параметры:
    автора строки и время создания"""

    def __new__(cls, init_string, author):
        instance = super().__new__(cls, init_string)
        instance.author = author
        instance.time_create = datetime.now()
        return instance


if __name__ == '__main__':
    my_string1 = MyString('Hello, world', 'Alex')
    print(my_string1, my_string1.author, my_string1.time_create, sep='\n')
