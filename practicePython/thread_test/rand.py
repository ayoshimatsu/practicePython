from concurrent.futures import (ProcessPoolExecutor, as_completed)
import numpy as np
import random

def use_numpy_random():
    np.random.seed()
    return np.random.random()

def use_standard_random():
    return random.random()

def main():
    with ProcessPoolExecutor() as e:
        futures = [e.submit(use_numpy_random) for _ in range(3)]

        for future in as_completed(futures):
            print(future.result())


if __name__ == '__main__':
    main()