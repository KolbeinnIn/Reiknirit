# Kolbeinn Ingólfsson
# Skilaverkefni 2 - FORR3RR05DU


# 1.


# 2.

"""
forrit skilgreinir fallið TVI og tekur inn tölu
    ef sú tala er stærri en 0
        þá kallar fallið á sig sjálft með tölunni deilt með tveimur
        og skrifar út töluna modulus 2
"""


# 3.
def d3(n):
    if n == 1:
        return n
    else:
        return (n * n) + d3(n - 1)


print("Dæmi 3")
print(d3(5), "\n-----------")


# 4.
def d4(n):
    if n == 1:
        print(n, end=" ")
    else:
        d4(n - 1)
        print(n * (n + 1) // 2, end=" ")


print("Dæmi 4")
d4(5)
print("\n-----------")

# 5.
"""
asd = 1209
summa = 0
for x in range(len(str(asd))):
    if str(asd)[x] == "0":
        print("asd")
    summa += int(str(asd)[x])
    print(str(asd)[x])
print(summa)

"""
def d8(n):
    if len(str(n)) == 1:
        return n
    else:
        if str(n)[1] == "0":
            return eval(str(n)[0]) + d8(eval(str(n)[2:]))
        else:
            return eval(str(n)[0]) + d8(eval(str(n)[1:]))


print(d8(1206))




