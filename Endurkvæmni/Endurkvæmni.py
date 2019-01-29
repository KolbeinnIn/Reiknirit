def d1(n):
    if n == 1:
        print(n)
    else:
        d1(n - 1)
        print(n)


def d2(n):
    if n == 1:
        print(n)
    else:
        print(n)
        d2(n - 1)


def d3(n):
    if n == 1:
        return n
    else:
        return n + d3(n - 1)


def d4(n):
    if n == 1:
        return n
    else:
        return n * d4(n - 1)


def d5(n):
    if n > 0:
        d5(n // 2)
        print(n % 2, end="")


def d6(strengur, fj = 0):
    if len(strengur) > 0:
        if strengur[0].isdigit():
            fj += 1
        d6(strengur[1:], fj)
    else:
        print(fj)

def d7(strengur, fj = 0):
    listi = ["a", "e", "i", "o", "u"]
    if len(strengur) > 0:
        if strengur[0] in listi:
            fj += 1
        d7(strengur[1:], fj)
    else:
        print(fj)

def d8(strengur):
    if len(strengur) > 0:
        print(strengur)
        d8(strengur[1:])


while True:
    print("\nDæmi 1-8 (9 til að hætta)")
    val = int(input("1-9:"))
    if val == 1:
        d1(int(input("Sláðu inn tölu: ")))
    elif val == 2:
        d2(int(input("Sláðu inn tölu: ")))
    elif val == 3:
        print(d3(int(input("Sláðu inn tölu: "))))
    elif val == 4:
        print(d4(int(input("Sláðu inn tölu: "))))
    elif val == 5:
        d5(int(input("Sláðu inn tölu: ")))
    elif val == 6:
        d6(input("Sláðu inn streng: "))
    elif val == 7:
        d7(input("Sláðu inn streng: "))
    elif val == 8:
        d8(input("Sláðu inn streng: "))
    elif val == 9:
        break
