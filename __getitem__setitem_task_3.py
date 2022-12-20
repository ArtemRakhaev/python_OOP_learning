class Integer:

    def __init__(self, start_value=0):
        self.__start_value = start_value

    @staticmethod
    def check_value(value):
        if type(value) != int:
            raise ValueError('должно быть целое число')

    @property
    def integer_value(self):
        return self.__start_value

    @integer_value.setter
    def integer_value(self, new_value):
        self.check_value(new_value)
        self.__start_value = new_value

    def __repr__(self):
        return str(self.__start_value)


class Array:

    def __init__(self, max_lenght, cell):
        self.cells = [cell(0) for _ in range(max_lenght)]
        self.max_length = max_lenght

    def __getitem__(self, item):
        self.check_index(item)
        return self.cells[item].integer_value

    def __setitem__(self, key, value):
        self.check_index(key)
        self.cells[key].integer_value = value

    def check_index(self, indx):
        if type(indx) != int or 0 > indx >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __repr__(self):
        return " ".join(map(str, self.cells))
