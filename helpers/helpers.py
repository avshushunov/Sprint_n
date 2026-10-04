import random
import string


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_unique_email():
    return f"{generate_random_string(10)}@mail.ru"