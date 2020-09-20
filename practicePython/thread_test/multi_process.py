import sys
import os
from concurrent.futures import (ProcessPoolExecutor, as_completed)
from concurrent.futures import (ThreadPoolExecutor, as_completed)
from ..my_decorator import decorator as deco

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
    else:
        return a

@deco.elapsed_time
def get_sequential(nums):
    for num in nums:
        print(fibonacci(num))

@deco.elapsed_time
def get_multi_process(nums):
    with ProcessPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]
        for future in as_completed(futures):
            print(future.result())

@deco.elapsed_time
def get_multi_thread(nums):
    with ThreadPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]
        for future in as_completed(futures):
            print(future.result())

def main():
    # print(os.cpu_count())
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    # get_multi_process(nums)
    # get_multi_thread(nums)
    get_sequential(nums)


if __name__ == "__main__":
    main()
