class Matrix:
    """Класс матрицы."""

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join('  '.join(map(str, row)) for row in self.my_list)

    def __add__(self, other):
        self.size_width = len(self.my_list)
        self.size_length = len(self.my_list[0])
        other.size_width = len(other.my_list)
        other.size_length = len(other.my_list[0])
        if self.size_width == other.size_width and self.size_length == other.size_length:
            return Matrix([[self.my_list[i][j] + other.my_list[i][j] for i in range(self.size_width)]
                           for j in range(self.size_length)])
        else:
            return None

    def summa(self):
        """Суммирует все элементы матрицы."""
        return sum([self.my_list[i][j] for i in range(len(self.my_list)) for j in range(len(self.my_list[0]))])

    def __eq__(self, other):
        """Сравнивает размеры матрицы и их поэлементное равенство."""
        self.size_width = len(self.my_list)
        self.size_length = len(self.my_list[0])
        other.size_width = len(other.my_list)
        other.size_length = len(other.my_list[0])
        if self.size_width == other.size_width and self.size_length == other.size_length:
            for i in range(len(self.my_list)):
                for j in range(len(self.my_list[0])):
                    if self.my_list[i][j] != other.my_list[i][j]:
                        return False
        return True

    def __gt__(self, other):
        """Больше ли сумма всех элементов или меньше."""
        return self.summa() > other.summa()

    def __ge__(self, other):
        """Не больше, меньше или равны ли суммы элементов."""
        return self.summa() <= other.summa()

    def __le__(self, other):
        """Не меньше, больше или равны ли суммы элементов."""
        return self.summa() >= other.summa()


if __name__ == '__main__':
    li = [[1, 2, 3], [4, 5, 6], [7, 8, 90]]
    li2 = [[1, 2, 3], [4, 5, 6], [7, 8, 99]]
    m = Matrix(li)
    n = Matrix(li2)
    print(m)
    print()
    print(n)
    print()
    print(m + n)

    print(m == n)
    print(m != n)
    print(m > n)
    print(m < n)
    print(m >= n)
    print(m <= n)
