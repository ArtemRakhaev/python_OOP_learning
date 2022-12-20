from random import sample, randint


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.__chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        lst_password = sample(self.__chars, randint(self.__min_length, self.__max_length))
        return "".join(lst_password)


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
psw = rnd()
lst_pass = [rnd() for _ in range(3)]
