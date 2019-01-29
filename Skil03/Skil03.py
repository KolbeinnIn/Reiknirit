# Kolbeinn Ingólfsson
# Skilaverkefni 3 Reiknirit
from string import *


# 1
def hanoi(n, a, b, c):
    if n == 1:
        print("Færa %s frá %s til %s" % (n, a, b))
    else:
        hanoi(n - 1, a, c, b)
        print("asd Færa %s frá %s til %s" % (n, a, b))
        hanoi(n - 1, c, b, a)

#1
hanoi(3, "A", "B", "C")

# 2

# 3
"""
    A)t.d. basic for lykkja
    B)t.d. for lykkja inni í for lykkju
    C)
"""

# 4
"""
print(ascii_lowercase)
print(digits)
print(hexdigits)
print(octdigits)
print(punctuation)
"""
