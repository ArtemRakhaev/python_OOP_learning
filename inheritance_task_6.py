class ListInteger(list):

    def __init__(self, numbers=None):
        if numbers is None:
            super().__init__([])
        else:
            map(self.validate_number, numbers)
            super().__init__(numbers)

    def __setitem__(self, key, value):
        if self.validate_number(value):
            super().__setitem__(key, value)

    def append(self, number):
        if self.validate_number(number):
            super().append(number)

    @staticmethod
    def validate_number(number):
        if type(number) != int:
            raise TypeError('можно передавать только целочисленные значения')
        return number
