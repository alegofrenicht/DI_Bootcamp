import random
import string as s

symbols = s.ascii_letters + s.digits + s.punctuation
key = ''.join([random.choice(symbols) for num in range(20)])


class Config:
    SECRET_KEY = key
