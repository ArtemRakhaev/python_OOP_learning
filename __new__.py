# 5 уникальных объектов, остальные содержат ссылку на 5-й объект
class SingletonFive:
    __count_objects = 0
    __last_object = None

    def __new__(cls, *args, **kwargs):
        if cls.__count_objects < 5:
            cls.__count_objects += 1
            cls.__last_object = super().__new__(cls)
            return cls.__last_object

        return cls.__last_object

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
