'''Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра'''

'''Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
'''


class Archive:
    '''Класс Archive, каждый экземпляр которого содержит в качестве параметров
    строку и число. Параметрами класса являются также списки строк и чисел всех созданных
    ранее экземпляров'''

    '''Вроде как __new__ без лишней необходимости не рекомендуется использовать, поэтому
    сделал просто с __init__. Тоже работает)'''
    string_list = []
    num_list = []

    def __init__(self, current_string, current_num):
        self.current_string = current_string
        self.current_num = current_num
        self.string_list.append(self.current_string)
        self.num_list.append(self.current_num)

    def __str__(self):
        return f'number = {self.current_num}, string: {self.current_string}'

    def __repr__(self):
        return f'Archive({self.current_string}, {self.current_num})'


if __name__ == '__main__':
    arch1 = Archive('first', 1)
    arch2 = Archive('second', 2)
    arch3 = Archive('third', 3)

    print(Archive.num_list, Archive.string_list)
    print(arch1.num_list, arch1.string_list)

    help(arch1)
