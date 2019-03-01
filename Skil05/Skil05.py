# Kolbeinn Ingólfsson
# Skilaverkefni 5 - Linked lists


class Vigur:
    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):

    # Þinn kóði hér

    # Fall sem skilar lengd
    def lengd(self):

    # Þinn kóði hér

    # Fall sem skilar hallatölu
    def halli(self):

    # Þinn kóði hér

    # Fall sem skilar þvervigri
    def þvervigur(self):

    # Þinn kóði hér

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):

    # Þinn kóði hér

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self, v):

    # Þinn kóði hér

    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self, v):


# Keyrsluforrit
v1 = Vigur(1, 3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: ", end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3, 1)
print("Horn milli vigra: ", v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: ", end=" ")
v3.prenta()
