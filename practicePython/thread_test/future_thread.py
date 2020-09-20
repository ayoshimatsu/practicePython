from concurrent.futures import (ThreadPoolExecutor, Future)
import time

def func():
    time.sleep(2)
    return 1


future = ThreadPoolExecutor().submit(func)
print(future.done())
print(future.result())