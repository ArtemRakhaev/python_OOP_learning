class Person:

    def __init__(self, fio, job, old, salary, year_job):
        self.__fio = fio
        self.__job = job
        self.__old = old
        self.__salary = salary
        self.__year_job = year_job
        self._atrs = tuple(self.__dict__)
        self.__iteration_indx = -1

    def __check_indx(self, indx):
        if type(indx) != int or not 0 <= indx <= 4:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_indx(item)
        return getattr(self, self._atrs[item])

    def __setitem__(self, key, value):
        self.__check_indx(key)
        setattr(self, self._atrs[key], value)

    def __iter__(self):
        self.__iteration_indx = -1
        return self

    def __next__(self):
        if self.__iteration_indx < len(self._atrs) - 1:
            self.__iteration_indx += 1
            return getattr(self, self._atrs[self.__iteration_indx])
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
