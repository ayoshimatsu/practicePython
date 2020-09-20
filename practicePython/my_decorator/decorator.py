from functools import wraps
import time


def overrides(interface_class):
    def overrider(method):
        assert (method.__name__ in dir(interface_class))
        return method
    return overrider

def elapsed_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - start}")
        return v
    return wrapper

def deco1(f):
    print('deco1 called')
    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)  # もとの関数を実行
        print('after exec')
        return v
    return wrapper

def deco3(z):
    def _deco3(f):
        def wrapper(*args, **kwargs):
            print('before exec', z)
            v = f(*args, **kwargs)  # もとの関数を実行
            print('after exec', z)
            return v
        return wrapper
    return _deco3

def deco4(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)  # もとの関数を実行
        print('after exec')
        return v
    return wrapper
