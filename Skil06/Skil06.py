# Kolbeinn Ingólfsson
# Heildun og flatarmál

import re


# dæmi 1 fall
def flatarmal_falls(fall, efri, nedri):
    if fall[0] != "-":
        fall = "+" + fall

    merki = []
    for x in fall:
        if x == "+" or x == "-":
            merki.append(x)

    fall_listi = re.split('[+-]', fall)
    try:
        fall_listi.remove("")
    except:
        pass

    heildad = []

    for x in fall_listi:
        if "x" in x:
            stadur = x.index("x")
            temp_listi1 = x[:stadur]
            temp_listi2 = x[stadur + 1:]
            if stadur == 0 and len(x) == 2:
                framan = str(1 / (int(x[stadur + 1]) + 1))
                veldi = str(int(x[stadur + 1]) + 1)
                heildad.append(framan + "*(x)**" + veldi)

            elif stadur != 0 and len(x) > 2:
                framan = str(int(x[:stadur]) / (int(x[stadur + 1]) + 1))
                veldi = str(int(x[stadur + 1]) + 1)
                heildad.append(framan + "*(x)**" + veldi)

            elif stadur == 0 and len(x) == 1:
                heildad.append("0.5*(x)**2")

            if len(temp_listi1) != 0 and len(temp_listi2) == 0:
                framan = str(int(x[:stadur]) / 2)
                heildad.append(framan + "*(x)**2")

        else:
            temp_s = fall_listi.index(x)
            temp = fall_listi[temp_s]
            heildad.append(str(temp) + "*(x)")

    heildad_fall = ""
    for x in range(len(heildad)):
        heildad_fall += merki[x] + heildad[x]

    listi = ["*", "(", ")"]
    pretty_heildad = heildad_fall
    for x in listi:
        pretty_heildad = pretty_heildad.replace(x, "")
    if pretty_heildad[0] == "+":
        pretty_heildad = pretty_heildad[1:]

    nytt_fall_a = heildad_fall.replace("x", str(nedri))
    nytt_fall_b = heildad_fall.replace("x", str(efri))

    flatarmal = round(abs(eval(nytt_fall_b) - eval(nytt_fall_a)), 5)
    return flatarmal


#########################################################################
# Dæmi 2 fall
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


with open("triangle.txt", "r") as f:
    skra = f.read()
    listi = skra.split("\n")


for x in range(len(listi)):
    listi[x] = listi[x].split(" ")
    for i in range(len(listi[x])):
        listi[x][i] = int(listi[x][i])

print(listi)

cache = {}
talna_listi = []
altsum = 0

def maxPath(listi, lina, index):
    summa = listi[lina][index]
    key = str(index)+","+str(lina)
    #print(key)
    if key in cache:
        return cache[key]
    if len(listi) == int(lina)+2:
        #print(listi[lina + 1][index], listi[lina + 1][index+1])
        gildi = summa + max(listi[lina + 1][index+1], listi[lina + 1][index])
        print(max(listi[lina + 1][index+1], listi[lina + 1][index]))
        cache[key] = gildi
        #print(cache)
        return gildi
    else:
        gildi = summa + max(maxPath(listi, lina+1, index+1), maxPath(listi, lina+1, index))
        #print(gildi-summa)
        cache[key] = gildi
        #print(cache)
        return gildi


print(maxPath(listi, 0, 0))
print(cache)

#print(listi)
"""print("Dæmi 1:")
fall1 = input("Sláðu inn fall f(x): ")
fall2 = input("Sláðu inn fall g(x): ")
efri1 = float(input("Sláðu inn x fyrir efri mörk: "))
nedri1 = float(input("Sláðu inn x fyrir neðri mörk: "))
print("--------------------------------")

flatarmal1 = flatarmal_falls(fall1, efri1, nedri1)
flatarmal2 = flatarmal_falls(fall2, efri1, nedri1)

print("Flatarmál f(x) og g(x) =", abs(round(flatarmal1 - flatarmal2, 5)))


print("\nDæmi 2:")
t = Tree()

print("----Find----")
print(8, t.find(8))
print("---Insert---")
print(6, t.insert(6))
print(2, t.insert(2))
print(3, t.insert(3))
print(7, t.insert(7))
print("----Find----")
print(8, t.find(8))
print("---Insert---")
print(8, t.insert(8))
print(8, t.find(8))
"""
