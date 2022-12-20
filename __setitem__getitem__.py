class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__total_attrs = len(kwargs)
        self.__attrs = tuple(self.__dict__.keys())

    def check_index(self, index):
         if type(index) != int or not (-self.__total_attrs <= index < self.__total_attrs):
             raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        self.check_index(key)
        setattr(self, self.__attrs[key], value)

    def __getitem__(self, item):
        self.check_index(item)
        return getattr(self, self.__attrs[item])


r = Record(pk=1, title='Python ООП', author='Балакирев')