from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_lenght, max_lenght):
        self.__min_lenght = min_lenght
        self.__max_lenght = max_lenght

    def __call__(self, string, *args, **kwargs):
        return self.__min_lenght <= len(string) <= self.__max_lenght


class CharsValidator:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, string, *args, **kwargs):
        return set(string) < set(self.__chars)
