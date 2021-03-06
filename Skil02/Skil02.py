# Kolbeinn Ingólfsson
# Skilaverkefni 2 - FORR3RR05DU


# 3.
def summa(n):
    if n == 1:
        return n
    else:
        return (n * n) + summa(n - 1)


print("Dæmi 3")
print(summa(5), "\n-----------")


# 4.
def runa(n):
    if n == 1:
        print(n, end=" ")
    else:
        runa(n - 1)
        print(n * (n + 1) // 2, end=" ")


print("Dæmi 4")
runa(5)
print("\n-----------")


# 5.
def þversumma(n):
    if "0" in str(n):
        n = str(n).replace("0", "")
        if len(n) == 0:
            return 0
        n = eval(n)
    if len(str(n)) == 1:
        return n
    else:
        return eval(str(n)[0]) + þversumma(eval(str(n)[1:]))


print("Dæmi 5")
for x in [1206, 1209, 1567, 10000006, 600, 0]:
    print("Þversumman af %s er:" % x, þversumma(x))
print("-----------")

print("Dæmi 6")


def samnefnari(n, m):
    if m == 0:
        return n
    else:
        return samnefnari(m, n % m)


print(samnefnari(int(input("Sláðu inn tölu 1:")), int(input("Sláðu inn tölu 2:"))))
print("-----------")
