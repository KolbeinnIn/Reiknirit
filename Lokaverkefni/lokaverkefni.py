# Kolbeinn Ingólfsson
# Lokaverkefni
# ÓÁKVEÐIÐ objective: 100% heildun.
import re

s = "sin(sin(sin(sin(x2+5x))))"
"""
stadur1 = 0
stadur2 = 0
for x in range(len(s)):
    if s[x] == "(":
        stadur1 = x+1
        break
s2 = ""
for x in range(len(s), 0, -1):
    s2 += s[x-1]
for x in range(len(s2)):
    if s2[x] == ")":
        stadur2 = x
        break
inni = s[stadur1:(len(s)-stadur2)]
undan = s[:stadur1-1]
print(undan)

print(inni)

fall = s
print(fall)
fall2 = ""
a1 = 0
a2 = 0
for x in range(len(fall)):
    if fall[x] == ")":
        a1 = x + 1
        break
for x in range(len(fall), 0, -1):
    print(fall)
    if fall[x-1] == "(":
        a2 = x-1
        break

print("Fall2 er", fall[a2:a1])


listi = ["abc", "asd", "efg", "hjk"]
stadur = listi.index("efg")
print(stadur)
print(listi[stadur])




---------------------
"""
import re


def master(func, args=""):
    if fall != "":
        return func(args)


def merkin(fall):
    try:
        m = re.search(".*\(([A-Za-z0-9_+-]+)\)", fall)
        print(m.group(1),"---------------------------------------")
        temp = "(%s)" % m.group(1)
        fall = fall.replace(temp, "")
        print(temp,"þetta er temp")
    except:
        pass

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
    listi = ["sin", "cos", "tan", "cot"]
    print(fall_listi, "falllistinn")
    for x in range(len(fall_listi)):
        for i in listi:
            #print(fall_listi[x], "falllisti x")
            if i == fall_listi[x]:
                fall_listi[x] = fall_listi[x] + temp
    #print(fall_listi,"loka fall listinn")
    return fall_listi, merki


def check_index(string):
    listi = ["sin", "cos", "tan", "cot"]
    for x in listi:
        if x in string:
            return x
    return False



def diffrun(fall):
    oll_merkin = merkin(fall)
    fall_listi = oll_merkin[0]
    print(fall_listi, "diffrun fær þennan")
    merki = oll_merkin[1]
    diffrad = []
    dicta = {"sin": "cos", "cos": "-sin"}
    for x in range(len(fall_listi)):
        if "x" in fall_listi[x]:
            i = fall_listi[x]
            sct = check_index(i)
            stadur = i.index("x")
            if sct:
                if sct in i:
                    print(i)
                    temp = ""
                    tempx = ""
                    eks = False
                    for j in i:
                        if eks and j != ")":
                            tempx += j
                        if j == "(":
                            eks = True
                        elif j != "(" and not eks:
                            temp += j
                    print(temp,"123")
                    print(tempx,"asd")
                    for key,value in dicta.items():
                        if key == temp:
                            if "+" in temp or "-" in temp:
                                kedja = "(%s)" % str(diffrun(tempx))
                                print(kedja, "kedja")
                            else:
                                kedja = str(diffrun(tempx))
                                print(kedja, "kedja")
                            temp = value+"(%s)*" % tempx + kedja
                            diffrad.append(temp)


            else:
                i = fall_listi[x]
                temp_listi1 = i[:stadur]
                temp_listi2 = i[stadur + 1:]
                if stadur == 0 and len(i) == 2:
                    # x2
                    framan = int(i[stadur + 1])
                    veldi = framan - 1
                    if veldi != 1 or veldi != 0:
                        if veldi == 1:
                            diffrad.append(str(framan) + "*x")
                        elif veldi == 0:
                            diffrad.append(str(framan))
                    else:
                        diffrad.append(str(framan) + "*x**" + str(veldi))

                elif stadur != 0 and len(i) > 2:
                    # 2x5
                    framan = str(int(i[:stadur]) * (int(i[stadur + 1:])))
                    print(framan)
                    veldi = str(int(i[stadur + 1:]) - 1)
                    if veldi == "1":
                        diffrad.append(framan + "*x")
                    else:
                        diffrad.append(framan + "*x**" + veldi)

                elif stadur == 0 and len(i) == 1:
                    # bara x með engri tölu fyrir framan né veldi.
                    diffrad.append("1")

                if len(temp_listi1) != 0 and len(temp_listi2) == 0:
                    # 5x í engu veldi
                    framan = str(int(i[:stadur]))
                    diffrad.append(framan)

        else:
            # 5 í engu veldi
            # gerir ekki neitt, else er bara hérna til að sýna að ef það er ekkert x þá dettur talan bara út
            pass

    diffrad_fall = ""
    for x in range(len(diffrad)):
        diffrad_fall += merki[x] + diffrad[x]

    # print(diffrad_fall)

    listi = ["*"]
    pretty_diffrad = diffrad_fall
    for x in listi:
        pretty_diffrad = pretty_diffrad.replace(x, "")
    if pretty_diffrad[0] == "+" or pretty_diffrad[:2] == "--":
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
                framan = str(int(x[:stadur]) / (int(x[stadur + 1:]) + 1))
                veldi = str(int(x[stadur + 1:]) + 1)
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
        fall = fall.replace(" ", "")

    print(master(func, fall))
    print()

