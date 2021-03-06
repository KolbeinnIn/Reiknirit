# Kolbeinn Ingólfsson
# Skilaverkefni 4 Reiknirit.
from time import perf_counter
from random import *


# 1
def fall(L):
    haesta = max(L)
    countL = [0] * (haesta + 1)
    resultL = [0] * len(L)

    for i in L:
        countL[i] += 1

    summa = 0
    for i in range(len(countL)):
        summa += countL[i]
        countL[i] = summa

    for i in range(len(L)):
        resultL[countL[L[i]] - 1] = L[i]
        countL[L[i]] -= 1

    return resultL


"""
randlisti = [randint(0, 1000) for x in range(1000)]
start = perf_counter()a
a = fall(randlisti)
print(perf_counter() - start)
print(a)
"""

print("""
Dæmi 1:
a) Fallið raðar lista með tölum.
b) Þetta reiknirit er kallað "Counting sort"
c) Flækjustig fallsins er O(n + k). k er bilið á milli stærsta staksins og því minnsta
""")

# randlisti = [randint(0, 10) for i in range(10)]
randlisti = [1, 2, 5, 6, 7, 8]
# 2
print("Dæmi 2:")


def linear(stak, listi):
    for x in range(len(listi)):
        if listi[x] == stak:
            return x
    return -1


print(randlisti)
# tala = int(input("linear(n): "))
tala = 9
a = linear(tala, randlisti)
if a != -1:
    print("Talan %d er í sæti %d" % (tala, a))
else:
    print("Talan %d er ekki í listanum" % tala)

print("")


# 3
def bin(tala, listi, low, high):
    if low <= high:
        mid = (high + low) // 2
        if tala == listi[mid]:
            return mid
        elif tala > listi[mid]:
            return bin(tala, listi, mid + 1, high)
        else:
            return bin(tala, listi, 0, mid - 1)
    else:
        return -1


print("Dæmi 3:")
listi = [x for x in range(10)]
#listi = [0, 1, 2, 4, 6, 7, 8, 9]
print(listi)
print(bin(10, listi, 0, len(listi)))

# 4
print("""
Dæmi 4:
a) flækjustigið er O(n) vegna þess að það er ein for lykkja í fallinu
b) O(log n) vegna þess að í hvert skipti sem fallið keyrir helmingast listinn
""")

rada_listi = [x for x in range(2, 11)]

# 5
print("Dæmi 5:")


def rada(tala, listi):
    if len(listi) == 0 or tala > listi[-1]:
        listi.append(tala)
        return True
    elif listi[0] > tala:
        listi.insert(0, tala)
        return True
    else:
        for x in range(len(listi)):
            if listi[x] <= tala <= listi[x + 1]:
                listi.insert(x + 1, tala)
                return True


print(rada_listi)
tala = int(input("Veldu tölu til að bæta í listann: "))
# tala = 5
print(rada(tala, rada_listi))
print(rada_listi)

# 6
print("\nDæmi 6:")


class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self, d):
        if self.value == d:
            return False

        elif self.value > d:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    def find(self, d):
        if self.value == d:
            return True

        elif self.value > d:
            if self.left:
                return self.left.find(d)
            else:
                return False
        else:
            if self.right:
                return self.right.find(d)
            else:
                return False


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def find(self, d):
        if self.root:
            return self.root.find(d)
        else:
            return False


t = Tree()

print("---Find 8---")
print(t.find(8))
print("---Insert---")
print(t.insert(6))
print(t.insert(2))
print(t.insert(3))
print(t.insert(7))
print("----Find----")
print(t.find(8))
print(t.insert(8))
print(t.find(8))
