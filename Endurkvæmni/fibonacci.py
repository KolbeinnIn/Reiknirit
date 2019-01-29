import datetime


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
while True:
    asd = int(input("Sláðu in tölu:"))
    timi1 = datetime.datetime.now()
    print(fib(asd))
    timi2 = datetime.datetime.now()
    print("Þetta tók:", timi2-timi1, "sek")
