from .b64 import encoder

print(encoder.str_to_base64("python"))

x = (1, 4, 5, 3, 2)
a = sorted(list(map(lambda i: i * 10, x)))

def gen_function(n):
    while n:
        yield n
        n -= 1


for i in gen_function(2):
    print(i)

gen = gen_function(5)
print(gen)
