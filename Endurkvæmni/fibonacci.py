from time import perf_counter

cache = {}


def fib(n):
    global cache
    value = 1
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fib(n - 1) + fib(n - 2)
    cache[n] = value
    return value


while True:
    asd = int(input("Sláðu inn tölu:"))
    timi1 = perf_counter()
    print(fib(35))
    timi2 = perf_counter()
    print("Þetta tók:", timi2 - timi1, "sek")
