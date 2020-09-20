import threading
from concurrent.futures import (ThreadPoolExecutor, wait)
from ..my_decorator import decorator as deco

class ThreadSafeCounter:
    lock = threading.Lock()

    def __init__(self):
        self.count = 0

    def increment(self):
        with self.lock:
            self.count = self.count + 1

@deco.elapsed_time
def count_up(counter_instance: ThreadSafeCounter):
    for _ in range(1000000):
        counter_instance.increment()


counter = ThreadSafeCounter()
threads = 2
with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up, counter) for _ in range(threads)]
    done, not_done = wait(futures)


print(f'{counter.count=:,}')
