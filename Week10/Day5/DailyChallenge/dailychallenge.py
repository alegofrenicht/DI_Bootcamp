# Instructions :
# Using the requests and time modules, create a function which returns the amount of time
# it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.
import requests
import time

def load_time(website):
    before = time.time()
    req = requests.get(website)
    if req.status_code == 200:
        after = time.time()
        duration = after - before
        return f"{website} access: {str(duration)[:4]} seconds"
    else:
        raise Exception(f"{req.status_code} ERROR")


print(load_time('https://www.google.com'))
print(load_time('https://www.ynet.co.il/'))
print(load_time('https://www.imdb.com/'))


