from random import sample
import string

def generate_code():
    return ''.join(sample(string.ascii_letters + string.digits, 15))