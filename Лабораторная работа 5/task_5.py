

def get_random_password(i=None) -> str:
    import string
    import random
    symbols_available = string.ascii_uppercase + string.ascii_lowercase + string.digits
    if i is None:
        random_list = random.sample(symbols_available, 8)
        random_password = ''.join(str(symbol) for symbol in random_list)
    else:
        random_list = random.sample(symbols_available, i)
        random_password = ''.join(str(symbol) for symbol in random_list)
    return random_password

print(get_random_password(4))
