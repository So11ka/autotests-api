import time
import random as rnd
import string

def random_email() -> str:
    return f"user{int(time.time())}@example.com"

def random_name() -> str:
    return rnd.choice(('Jonh', 'Patricia', 'May', 'Elizabet', 'Victor', 'Dack'))

def random_surname() -> str:
    return rnd.choice(('Parker', 'Norton', 'Adams', 'Watson', 'Murphy', 'Jackson'))

def random_password(len_pass=12) -> str:
    result = string.ascii_letters + string.digits
    return ''.join(rnd.choices(result, k=len_pass))