import re
import math

def master(func, args=""):
    if args != "":
        return func(args)


def merkin(fall):
    try:
        """
        m = re.search(".*\(([A-Za-z0-9_+-]+)\)", fall)
        print(m.group(1),"---------------------------------------")
        temp = "(%s)" % m.group(0)
        fall = fall.replace(temp, "")
        print(temp)
        """
        stadur1 = 0
        stadur2 = 0
        s = fall
        for x in range(len(s)):
            if s[x] == "(":
                stadur1 = x + 1
                break
        s2 = ""
        for x in range(len(s), 0, -1):
            s2 += s[x - 1]
        for x in range(len(s2)):
            if s2[x] == ")":
                stadur2 = x
                break
        undan = s[:stadur1 - 1]
    except:
        pass

    if fall[0] != "-":
        fall = "+" + fall

    merki = []
    for x in fall:
        if x == "+" or x == "-":
            merki.append(x)

    fall2 = ""
    a1 = 0
    a2 = 0
    for x in range(len(fall)):
        if fall[x] == ")":
            a1 = x + 1
            break
    for x in range(len(fall), 0, -1):
        if fall[x - 1] == "(":
            a2 = x - 1
            break

    fall2 = fall[a2 + 1:a1 - 1]

    # fall_listi = re.split('[+-]', fall)
    if fall[0] == "+":
        fall = fall[1:]
    # if "/" in fall or "*" in fall:

    #print("pre", fall)
    if check_index(fall):
        #print("post", fall)
        fall_listi = [fall]
    else:
        fall_listi = re.split('[+-]', fall)
        for x in range(len(fall_listi)):
            fall_listi[x] = fall_listi[x].replace(")", "")
            fall_listi[x] = fall_listi[x].replace("(", "")

    try:
        fall_listi.remove("")
    except:
        pass

    listi = ["sin", "cos", "tan", "cot", "ln"]
    for x in range(len(fall_listi)):
        for i in listi:
            if i == fall_listi[x]:
                fall_listi[x] = fall_listi[x] + "(%s)" % fall2

    # print(fall_listi,"þetta er fall listinn")
    return fall_listi, merki


def check_index(string):
    listi = ["sin", "cos", "tan", "cot", "ln"]
    for x in listi:
        if x in string:
            return x
    return False


def u_v(fall):
    if "/" in fall:
        u_v_listi = fall.split('/')
        u = u_v_listi[0]
        v = u_v_listi[1]

        #print("Nú diffast u")
        du = diffrun(u)
        #print("Nú diffast v")
        dv = diffrun(v)

        """print("u", u)
        print("du", du)
        print("v", v)

        print("dv", dv)"""


        bandstrik = ""
        for x in range(len("%s*%s - %s*%s" % (du, v, u, dv)) + 1):
            bandstrik += "-"

        formula = "%s*%s) - %s*(%s)\n%s\n(%s)^2" % (du, v, u, dv, bandstrik, v)

    elif "*" in fall:
        u_v_listi = fall.split('*')
        u = u_v_listi[0]
        v = u_v_listi[1]

        du = diffrun(u)
        dv = diffrun(v)
        """
        print("u", u)
        print("du", du)
        print("v", v)
        print("dv", dv)
        """
        formula = "%s*%s) + %s*(%s" % (du, v, u, dv)

    #print("u og v reglan", formula)
    return formula


def diffrun(fall):
    oll_merkin = merkin(fall)
    fall_listi = oll_merkin[0]
    merki = oll_merkin[1]
    diffrad = []
    diffrad_uv = []
    #print("listinn sem diffrun fær", fall_listi)
    dicta = {"sin": "cos", "cos": "-sin", "tan": "sec2", "cot": "-csc2", "ln": "1/"}
    # print(fall_listi, "diffrun fær þennan")
    for x in range(len(fall_listi)):
        if "x" in fall_listi[x]:
            if "/" in fall_listi[x] or "*" in fall_listi[x]:
                diffrad.append(u_v(fall_listi[x]))
            else:
                i = fall_listi[x]
                sct = check_index(i)
                stadur = i.index("x")
                if sct:
                    if sct in i:
                        temp = ""
                        tempx = ""
                        eks = False
                        teljari = 0  # telur hversu margir ) eru komnir
                        teljari1 = -1  # telur hversu margir ( eru komnir
                        teljari2 = i[:-1].count(")")

                        for j in range(len(i)):
                            # print(eks, teljari < teljari1)
                            if eks and teljari <= teljari1:
                                if teljari == teljari1 and teljari != 0:
                                    pass
                                else:
                                    tempx += i[j]
                                    # print("went in", tempx)

                            # if i[j] == "(" and eks:

                            if i[j] == "(":  # teljari 1 (
                                eks = True
                                teljari1 += 1

                            if i[j] == ")" and eks:  # teljari )
                                teljari += 1



                            elif i[j] != "(" and not eks:
                                temp += i[j]
                                # print(temp)

                        if not check_index(tempx) and tempx[-1] == ")":  # confirmed rétt if setning og allt inni í henni
                            # print("súper dúper tempx", tempx)
                            tempx = tempx[:-1]

                        for key, value in dicta.items():
                            if key == temp:
                                if "+" in temp or "-" in temp:
                                    kedja = "(%s)" % str(diffrun(tempx))
                                else:
                                    kedja = str(diffrun(tempx))
                                if "/" in value:
                                    temp = "(%s)" % (kedja) + value + tempx
                                else:
                                    temp = value + "(%s)*" % tempx + kedja

                                diffrad.append(temp)

                else:
                    i = fall_listi[x]
                    #print("fall listinn", fall_listi)
                    i = i.replace("(", "")
                    i = i.replace(")", "")

                    temp_listi1 = i[:stadur]
                    temp_listi2 = i[stadur + 1:]
                    #print(temp_listi1)
                    #print(temp_listi2)
                    #print("i er", i)
                    if len(temp_listi1) != 0 and len(temp_listi2) == 0 and len(i) != 1:
                        # 5x í engu veldi
                        framan = str(int(i[:stadur]))
                        diffrad.append(framan)

                    if stadur == 0 and len(i) >= 2:
                        # x2, x3, x27
                        framan = int(i[stadur + 1:])
                        veldi = framan-1
                        if veldi != 0:
                            if veldi == 1:
                                #print("asd", i)
                                #print("asdasdasd " + str(framan) + "*x")
                                #print("veldi", veldi)
                                diffrad.append(str(framan) + "*x")

                            elif veldi > 1:
                               diffrad.append(str(framan) + "*x**" + str(veldi))
                        else:
                            diffrad.append(str(framan) + "*x**" + str(veldi))

                    elif stadur != 0 and len(i) > 2:
                        # 2x5
                        framan = str(int(i[:stadur]) * (int(i[stadur + 1:])))
                        veldi = str(int(i[stadur + 1:]) - 1)
                        if veldi == "1":
                            diffrad.append(framan + "*x")
                        else:
                            diffrad.append(framan + "*x**" + veldi)


        else:
            # 5 í engu veldi
            # gerir ekki neitt, else er bara hérna til að sýna að ef það er ekkert x þá dettur talan bara út
            pass

    diffrad_fall = ""
    #print("+=diffrad", diffrad)
    for x in range(len(diffrad)):
        diffrad_fall += merki[x] + diffrad[x]

    listi = ["*"]
    #print("diffrad_fall", diffrad_fall)
    pretty_diffrad = diffrad_fall

    if diffrad_fall != "":
        if check_index(diffrad_fall):
            if diffrad_fall[-1] == "*":
                diffrad_fall = diffrad_fall[:-1]
                #print("remove last star", diffrad_fall)
            #(diffrad_fall)
            asd = False


            try:
                asd = diffrad_fall.index(")*")
            except:
                pass
            if asd:
                temp1 = diffrad_fall[:asd+1]
                temp2 = diffrad_fall[asd+2:]
                temp1 = temp1.replace("*", "")
                temp2 = temp2.replace("*", "")
                #print("potential svigi", temp2)
                nytt = "%s(%s)" % (temp1,temp2)
                pretty_diffrad = nytt
                #print("nýtt", nytt)


    try:
        if pretty_diffrad[0] == "+" or pretty_diffrad[:2] == "--":
            pretty_diffrad = pretty_diffrad[1:]
    except:
        pass

    return pretty_diffrad

# returnar heilduðu falli ekki pretty printað, dæmi: 2*x**2 væri 2x2 pretty printað, þetta er bara til að geta notað eval() fallið.
def heildun(fall):
    merkin1 = merkin(fall)
    fall_listi = merkin1[0]
    merki = merkin1[1]

    heildad = []

    for x in fall_listi:
        if "x" in x:
            stadur = x.index("x")
            temp_listi1 = x[:stadur]
            temp_listi2 = x[stadur + 1:]
            if stadur == 0 and len(x) == 2:
                rounded = "1/" +str((int(x[stadur + 1]) + 1))
                framan = str(rounded)
                veldi = str(int(x[stadur + 1]) + 1)
                heildad.append(" " + framan + "*(x)**" + veldi + " ")

            elif stadur != 0 and len(x) > 2:
                framan = str(int(x[:stadur]))+ "/" +str((int(x[stadur + 1:]) + 1))
                veldi = str(int(x[stadur + 1:]) + 1)
                heildad.append(" " + framan + "*(x)**" + veldi + " ")

            elif stadur == 0 and len(x) == 1:
                heildad.append(" 0.5*(x)**2 ")

            if len(temp_listi1) != 0 and len(temp_listi2) == 0:
                framan = int(x[:stadur]) / 2
                if framan == 1:
                    heildad.append(" (x)**2 ")
                else:
                    framan = str(framan)
                    heildad.append(" " + framan + "*(x)**2 ")

        else:
            temp_s = fall_listi.index(x)
            temp = fall_listi[temp_s]
            print("scooby snacks",temp)
            if temp == "1":
                heildad.append("x")
            elif temp == "0":
                heildad.append(" ")
            else:
                heildad.append(temp + "*(x)")

    heildad_fall = ""
    for x in range(len(heildad)):
        heildad_fall += merki[x] + heildad[x]

    return heildad_fall

def rummal_snuda(fall):
    asd = heilda(fall)
    print(asd)

    return "Rúmmál: " + str(math.pi * (heilda(fall)))

def heilda(fall):
    if type(fall) is tuple:
        fall1 = fall[0]
        fall2 = fall[1]
        efri = fall[2]
        nedri = fall[3]
        rummal_YN = False
        try:
            rummal_YN = fall[4]
        except:
            pass

        heildad_fall_1 = heildun(fall1)
        heildad_fall_2 = heildun(fall2)
        nytt_fall_a1 = heildad_fall_1.replace("x", str(nedri))
        nytt_fall_b1 = heildad_fall_1.replace("x", str(efri))

        nytt_fall_a2 = heildad_fall_2.replace("x", str(nedri))
        nytt_fall_b2 = heildad_fall_2.replace("x", str(efri))

        flatarmal1 = round(abs(eval(nytt_fall_b1) - eval(nytt_fall_a1)), 5)
        flatarmal2 = round(abs(eval(nytt_fall_b2) - eval(nytt_fall_a2)), 5)
        if rummal_YN:
            return abs(round(flatarmal1 - flatarmal2, 5))
        else:
            return "Flatarmál á milli f(x) og g(x) er %s" % abs(round(flatarmal1 - flatarmal2, 5))

    else:
        fall_listi = merkin(fall)
        heildad_fall = heildun(fall)

    listi = ["*", "(", ")"]
    pretty_heildad = heildad_fall
    for x in listi:
        pretty_heildad = pretty_heildad.replace(x, "")
    if pretty_heildad[0] == "+":
        pretty_heildad = pretty_heildad[1:]

    return pretty_heildad

val_listi = ["Heilda fall", "Flatarmál milli falla", "Diffra fall", "Rúmmál snúða"]

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
        func = heilda
        print("Dæmi um fall: x2+5x+3")
        fall = input("Sláðu inn fall:")

    elif val == 2:
        func = heilda
        print("Dæmi um fall: x2+5x+3")
        fall1 = input("Sláðu inn fall fyrir f(x):")
        fall2 = input("Sláðu inn fall fyrir g(x):")
        efri = float(input("Sláðu inn x fyrir efri mörk: "))
        nedri = float(input("Sláðu inn x fyrir neðri mörk: "))
        fall1 = fall1.replace(" ", "")
        fall2 = fall2.replace(" ", "")
        fall = (fall1, fall2, efri, nedri)

    elif val == 3:
        func = diffrun
        print("Dæmi um fall: x2+5x+3")
        print("Dæmi um fall: sin(cos(x2+5x+3))")
        fall = input("Sláðu inn fall: ")
        print()
        fall = fall.replace(" ", "")
    elif val == 4:
        func = rummal_snuda
        print("ATH! Vegna þess að það er tímafrekt og flókið þarft þú að setja fallið í annað veldi")
        print("Dæmi um fall: x+1")
        print("Fallið yrði þá: x2+2x+1")
        fall1 = input("Sláðu inn fall fyrir f(x):")
        fall2 = "0"
        efri = float(input("Sláðu inn x fyrir efri mörk: "))
        nedri = float(input("Sláðu inn x fyrir neðri mörk: "))
        fall1 = fall1.replace(" ", "")
        fall2 = fall2.replace(" ", "")
        fall = (fall1, fall2, efri, nedri, True)

    else:
        print("Rangur innsláttur, reyndu aftur\n")
    if val == 1:
        utkoma = master(func, fall)
        if utkoma == " ":
            print("C")
        else:
            print(master(func, fall)+"+ C")
    else:
        print(master(func, fall))
    print()
