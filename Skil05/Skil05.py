# Kolbeinn Ingólfsson
# Skilaverkefni 5 - Linked lists og Vigrar
import math


class Node:
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # Endurkvæmt fall sem bætir aftast á listann.
    def append(self, d):
        if self.nxt:
            return self.nxt.append(d)
        else:
            curr = Node(d)
            self.nxt = curr
            curr.prv = self
            return True

    # Endurkvæmt fall sem og prentar listann.
    def printList(self):
        print(self.data)
        if self.nxt:
            return self.nxt.printList()

    # Endurkvæmt fall sem og prentar listann frá Head til enda
    def find(self, d):
        if self.data == d:
            return True
        elif self.nxt:
            return self.nxt.find(d)
        else:
            return False

    # Endurkvæmt fall sem eyðir ákveðnum hnút úr lista
    def delete(self, d):
        if self.data == d:
            self.prv.nxt = self.nxt
            if self.nxt:
                self.nxt.prv = self.prv
            self.nxt = None
            self.prv = None
            return True

        else:
            return self.nxt.delete(d)


class DLL:  # DLL = Dobule Linked List
    def __init__(self):
        self.head = None

    # Bætir við fremst á listann, hnúturinn verður Head -> förum ekki í Node klasann.  Þú úrfærir fallið í þessum klasa
    def push(self, d):
        temp = Node(d)
        temp.nxt = self.head
        self.head.prv = temp
        self.head = temp
        return True

    # Bætir við aftast á listann -> kallar á endurkvæmnt fall í Node.  Fallið er þegar útfært í Node klasa
    def append(self, d):
        if self.head:
            return self.head.append(d)
        else:
            self.head = Node(d)
            return True

    # Prentar listann allan á skjá -> kallar á endurkvæmt fall í Node, þú útfærir printList í Node.  Notaðu endurkvæmni.
    def printList(self):
        if self.head:
            self.head.printList()
        else:
            print("Empty list!")

    # Kallar á endurkvæmt fall í Node klasanum, finnur ákveðinn hnút.  Þú útfærir fallið find í Node klasanum.  Notaðu endurkvæmni.
    def find(self, d):
        if self.head:
            return self.head.find(d)
        else:
            return False

    # Kallar á endurkvæmt fall í Node klasanum, finnur ákveðinn hnút og eyðir.  Þú útfærir fallið delete í Node klasanum.  Notaðu endurkvæmni.
    def delete(self, d):
        try:
            if self.head is None:
                return False
            elif self.head.data == d:
                self.head = self.head.nxt
                if self.head:
                    self.head.prv.nxt = None
                    self.head.prv = None
                return True

            else:
                return self.head.delete(d)
        except:
            return False


dbl = DLL()
print("---Append---")
print(dbl.append(5))
print(dbl.append(7))
print("----Push----")
print(dbl.push(1))
print(dbl.push(0))
print("Append")
print(dbl.append(10))
print("----Print---")
dbl.printList()
print("---Delete---")
print(dbl.delete(15))
print("----Find----")
print(dbl.find(1))
print(dbl.find(7))
print("----Print---")
dbl.printList()
print("-----------")


class Vigur:
    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def prenta(self):
        print("(%d, %d)" % (self.x, self.y))

    def lengd(self):
        l = round(math.sqrt((self.x ** 2) + (self.y ** 2)), 3)
        return l

    def halli(self):
        return round(self.y / self.x, 2)

    def þvervigur(self):
        return Vigur(-self.y, self.x)

    def stefnuhorn(self):
        x = self.x
        y = self.y
        if x < 0 and y < 0:
            return round(math.degrees(math.atan(y / x)) - 180, 2)
        elif x < 0:
            return round(180 - math.degrees(-math.atan(y / x)), 2)
        else:
            return round(math.degrees(math.atan(y / x)), 2)

    def horn(self, v):
        a = self.x * v.x
        b = self.y * v.y
        a1 = math.sqrt((self.x ** 2) + (self.y ** 2))
        b1 = math.sqrt((v.x ** 2) + (v.y ** 2))
        formula = (a + b) / (a1 * b1)
        h = round(math.degrees(math.acos(formula)), 2)
        return h

    def summa(self, v):
        return Vigur(self.x + v.x, self.y + v.y)


# Keyrsluforrit
print("-------------------Vigrar-------------------")
v1 = Vigur(4, 4)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: ", end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(1, 0)
print("Horn milli vigra: ", v2.horn(v1))
v3 = v1.summa(v2)
print("Summa:", end=" ")
v3.prenta()

