# Kolbeinn Ingólfsson
# Skilaverkefni 3 Reiknirit.
from string import *
from time import perf_counter
import sys


# 1
def hanoi(n, a, b, c):
    if n == 1:
        print("Færa %s frá %s til %s" % (n, a, b))
    else:
        hanoi(n - 1, a, c, b)
        print("asd Færa %s frá %s til %s" % (n, a, b))
        hanoi(n - 1, c, b, a)


# 1
print("Dæmi 1")
hanoi(3, "A", "B", "C")

# 2
"""
O(2^n)

"""

# 3
"""
    A)t.d. basic for lykkja
    B)t.d. for lykkja inni í for lykkju
    C)forrit sem notar divide and conquer t.d. að skipta lista í tvennt og að leita í einum þangað til það finnur hvað það var að leita að
"""

# 4
"""
    26!
__________
(26-n)!*n!
"""


alisti = ascii_lowercase
listi2 = []
sys.setrecursionlimit(10000)


def strengur(n, s="", t=0):
    if n > 26:
        print("það eru bara 26 stafir í enska stafrófinu þannig nú breytum við í það")
        n = 26
    if n > 0:
        for x in range(t, len(alisti)):
            if n == 1:
                listi2.append(s + alisti[x])
            t += 1
            strengur(n - 1, s + alisti[x], t)

print("Dæmi 4")
n = int(input("strengur(n):"))
strengur(n)
print(listi2)

print("Dæmi 5")
listi2.reverse()
print(listi2)

tlisti = [5, 2, 7, 8, 4]


def part(listi, low, high):
    i = low-1
    for x in range(low, high):
        if listi[x] <= listi[high]:
            i += 1
            temp = listi[x]
            listi[x] = listi[i]
            listi[i] = temp

    temp = listi[high]
    listi[high] = listi[i + 1]
    listi[i+1] = temp
    return i+1


def quicksort(listi, low, high):
    if low < high:
        index = part(listi, low, high)
        quicksort(listi, low, index-1)
        quicksort(listi, index+1, high)


quicksort(listi2, 0, len(listi2)-1)
#part(listi2, 0, len(listi2)-1)
print(listi2)


"""
print(ascii_lowercase)
print(digits)
print(hexdigits)
print(octdigits)
print(punctuation)
"""
