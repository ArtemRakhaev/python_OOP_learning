class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


class LessonItem:
    __VALUES = {'title': str, 'practices': int, 'duration': int}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __delattr__(self, item):
        if item == 'title' or item == 'practices' or item == 'duration':
            raise ValueError('нельзя удалять атрибут')

    def __setattr__(self, key, value):
        if key in self.__VALUES and type(value) is self.__VALUES[key]:
            if (key == 'practices' or key == 'duration') and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in self.__VALUES:
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)
