import time
import random as rnd
import string

def random_email() -> str:
    return f"user{int(time.time())}@example.com"

def random_name(name: str=None) -> str:
    names = ['Jonh', 'Patricia', 'May', 'Elizabet', 'Victor', 'Dack']
    return rnd.choice(names) if name is None else rnd.choice([i for i in names if i != name])

def random_surname(surname: str=None) -> str:
    surnames = ['Parker', 'Norton', 'Adams', 'Watson', 'Murphy', 'Jackson']
    return rnd.choice(surnames) if surname is None else rnd.choice([i for i in surnames if i != surname])

def random_password(len_pass=12) -> str:
    result = string.ascii_letters + string.digits
    return ''.join(rnd.choices(result, k=len_pass))