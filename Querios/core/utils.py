import random
import string


ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    """
    Function to generate a random string for uses of creating a unique slug
    used in signals.py file.
    """
    return ''.join(random.choice(chars) for _ in range(length))