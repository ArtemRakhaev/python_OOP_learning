class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not self.check_value(value):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        else:
            setattr(instance, self.name, value)

    @staticmethod
    def check_value(value):
        return isinstance(value, float)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
cell_value = 1.0

for i in range(5):
    for j in range(3):
        table.cells[i][j].value = cell_value
        cell_value += 1.0