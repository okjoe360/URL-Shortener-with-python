import string
import random

def short_generator():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return res