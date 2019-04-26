import re


def master(func, args=""):
    if fall != "":
        return func(args)



def merkin(fall):
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
    return fall_listi, merki


def check_index(string):
    listi = ["sin", "cos", "tan", "cot"]
    for x in listi:
        if x in string:
            return x
    return False

print(check_index("asdasdasdsinasdasdasd"))

def diffrun(fall):
    oll_merkin = merkin(fall)
    fall_listi = oll_merkin[0]
    merki = oll_merkin[1]
    diffrad = []
    for x in fall_listi:
        if "x" in x:
            sct = check_index(x)
            stadur = x.index("x")
            if sct:
                if sct in x:
                    stadur2 = x.index(sct)
                    print(stadur2, "bøísår")


            temp_listi1 = x[:stadur]
            temp_listi2 = x[stadur + 1:]
            if stadur == 0 and len(x) == 2:
                #x2
                framan = int(x[stadur + 1])
                veldi = framan-1
                if veldi != 1 or veldi != 0:
                    if veldi == 1:
                        diffrad.append(str(framan) + "*(x)")
                    elif veldi == 0:
                        diffrad.append(str(framan))
                else:
                    diffrad.append(str(framan) + "*(x)**" + str(veldi))

            elif stadur != 0 and len(x) > 2:
                #2x5
                framan = str(int(x[:stadur]) * (int(x[stadur + 1])))
                print(framan)
                veldi = str(int(x[stadur + 1]) - 1)
                diffrad.append(framan + "*(x)**" + veldi)

            elif stadur == 0 and len(x) == 1:
                #bara x með engu
                diffrad.append("1")

            if len(temp_listi1) != 0 and len(temp_listi2) == 0:
                #5x í engu veldi
                framan = str(int(x[:stadur]))
                diffrad.append(framan)

        else:
            #5 í engu veldi
            # gerir ekki neitt, else er bara hérna til að sýna að ef það er ekkert x þá dettur talan bara út
            pass

    diffrad_fall = ""
    for x in range(len(diffrad)):
        diffrad_fall += merki[x] + diffrad[x]

    #print(diffrad_fall)

    listi = ["*", "(", ")"]
    pretty_diffrad = diffrad_fall
    for x in listi:
        pretty_diffrad = pretty_diffrad.replace(x, "")
    if pretty_diffrad[0] == "+":
        pretty_diffrad = pretty_diffrad[1:]

    return pretty_diffrad





def flatarmal_falls(fall, efri, nedri):
    fall_listi = merkin(fall)

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


"""print("Dæmi 1:")
fall1 = input("Sláðu inn fall f(x): ")
fall2 = input("Sláðu inn fall g(x): ")
efri1 = float(input("Sláðu inn x fyrir efri mörk: "))
nedri1 = float(input("Sláðu inn x fyrir neðri mörk: "))
print("--------------------------------")

flatarmal1 = flatarmal_falls(fall1, efri1, nedri1)
flatarmal2 = flatarmal_falls(fall2, efri1, nedri1)

print("Flatarmál f(x) og g(x) =", abs(round(flatarmal1 - flatarmal2, 5)))
"""

val_listi = ["Heilda fall", "Flatarmál milli falla", "Staðbundin útgildi á falli", "Diffra fall", "Rúmmál snúða"]

while True:
    for x in range(len(val_listi)):
        print(x + 1, val_listi[x])
    print("")
    while True:
        try:
            val = int(input("Veldu lið: "))
            break
        except ValueError:
            print("Rangur innsláttur, reyndu aftur\n")

    func = ""
    fall = ""
    if val == 1:
        pass
    elif val == 2:
        pass
    elif val == 3:
        pass
    elif val == 4:
        func = diffrun
        print("Dæmi um fall: x2+5x+3")
        fall = input("Sláðu inn fall: ")

    print(master(func, fall))
    print()

