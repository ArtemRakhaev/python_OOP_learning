class Validator:

    def __call__(self, *args, **kwargs):
        data, *other = args
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')

    def _is_valid(self, data):
        return True


class IntegerValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        super()._is_valid(data)
        return type(data) is int and (self.min_value <= data <= self.max_value)


class FloatValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        super()._is_valid(data)
        return type(data) is float and (self.min_value <= data <= self.max_value)
