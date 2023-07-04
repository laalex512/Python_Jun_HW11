import random


class Matrix:

    def __init__(self, rows, cols):
        self.num_list = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]

    def __mul__(self, other):
        rows1 = len(self.num_list)
        cols1 = len(self.num_list[0])
        rows2 = len(other.num_list)
        cols2 = len(other.num_list[0])

        if cols1 != rows2:
            raise ValueError("The number of columns in matrix1 must be equal to the number of rows in matrix2.")

        result = Matrix(rows1, cols2)

        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result.num_list[i][j] += self.num_list[i][k] * other.num_list[k][j]

        return result

    def __add__(self, other):
        if len(self.num_list) != len(other.num_list) or len(self.num_list[0]) != len(other.num_list[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")

        rows = len(self.num_list)
        cols = len(self.num_list[0])

        result = Matrix(rows, cols)

        for i in range(rows):
            for j in range(cols):
                result.num_list[i][j] = self.num_list[i][j] + other.num_list[i][j]

        return result

    def __sub__(self, other):
        if len(self.num_list) != len(other.num_list) or len(self.num_list[0]) != len(other.num_list[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")

        rows = len(self.num_list)
        cols = len(self.num_list[0])

        result = Matrix(rows, cols)

        for i in range(rows):
            for j in range(cols):
                result.num_list[i][j] = self.num_list[i][j] - other.num_list[i][j]

        return result

    def __str__(self):
        result = ''
        for i in range(len(self.num_list)):
            for num in self.num_list[i]:
                result += ' ' + str(num)
            result += '\n'
        return result


if __name__ == '__main__':
    m1 = Matrix(3, 3)
    m2 = Matrix(3, 3)
    print(m1, m2, m1 + m2, m1 - m2, m1 * m2, sep='\n')
