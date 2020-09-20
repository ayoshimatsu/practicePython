from contextlib import contextmanager

@contextmanager
def point(**kwargs):
    print("__enter__ was called")
    value = kwargs
    try:
        yield value
    except Exception as e:
        print(e)
        raise
    finally:
        print("__exit__ was called")
        print(value)

class ContextManager:
    def __enter__(self):
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with ContextManager() as f:
    print(f)

with point(x=1, y=2) as p:
    print(p)
    p["z"] = 3
