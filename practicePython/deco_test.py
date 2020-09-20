from functools import lru_cache
from dataclasses import dataclass
from time import sleep
from .my_decorator import decorator as deco

@lru_cache(maxsize=32)
def heavy_function(n):
    sleep(3)
    print(n + 1)

@dataclass(frozen=True)
class Fruit:
    name: str
    price: int = 0

@deco.deco3(z=3)
def func(x, y):
    print('exec')
    return x, y

@deco.deco4
def func_test():
    print("exec")

@deco.elapsed_time
def func_time(n):
    return sum(i for i in range(n))


print(f'{func_time(100000) = :,}')
# print(func_test.__name__)
# func_test()
# print(func.__name__)
# print(func(1, 3))
