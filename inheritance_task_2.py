class Thing:
    __id = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = self.__generate_id()
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    @classmethod
    def __generate_id(cls):
        Thing.__id += 1
        return Thing.__id

    def get_data(self):
        return tuple(self.__dict__.values())


class Table(Thing):

    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):

    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
book.get_data()
