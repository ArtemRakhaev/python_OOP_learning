class Car:
    def __init__(self):
        self.__model = None

    @staticmethod
    def __check_model(string):
        return type(string) == str and 2 <= len(string) <= 100

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__check_model(model):
            self.__model = model
