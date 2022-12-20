from string import ascii_letters, digits
from random import choices, randint


class EmailValidator:
    CHARS_FOR_EMAIL = ascii_letters + digits + "_."
    CHARS_FOR_CORRECT = CHARS_FOR_EMAIL + "@"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            return len(email.split("@")[0]) <= 100 and len(email.split("@")[1]) <= 50 and ".." not in email and "." in \
                   email.split("@")[1] and len(email.split("@")) == 2 and set(email) < set(cls.CHARS_FOR_CORRECT)
        return False

    @classmethod
    def get_random_email(cls):
        random_email = f'{"".join(choices(cls.CHARS_FOR_EMAIL, k=randint(7, 25)))}@gmail.com'
        if random_email[0] != ".":
            return random_email
        else:
            return random_email[1:]

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


em = EmailValidator.get_random_email()
