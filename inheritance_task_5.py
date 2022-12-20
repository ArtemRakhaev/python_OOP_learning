class Validator:

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, *args, **kwargs):
        data, *other = args
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return True

    def _is_valid(self, data):
        return True


class ProtoValidator(Validator):
    data_type = None

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def _is_valid(self, data):
        super()._is_valid(data)
        return type(data) is self.data_type and (self.min_value <= data <= self.max_value)


class IntegerValidator(ProtoValidator):
    data_type = int


class FloatValidator(ProtoValidator):
    data_type = float
