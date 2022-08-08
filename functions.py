import random
from constants import *

chars = ""

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    print(password)


