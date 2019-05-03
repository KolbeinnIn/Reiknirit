import re


def master(func, args=""):
    if fall != "":
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
                stadur1 = x+1
                break
        s2 = ""
        for x in range(len(s), 0, -1):
            s2 += s[x-1]
        for x in range(len(s2)):
            if s2[x] == ")":
                stadur2 = x
                break
        undan = s[:stadur1-1]
    except:
        pass
        print("fór í except í merkin")


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
        if fall[x-1] == "(":
            a2 = x-1
            break

    fall2 = fall[a2+1:a1-1]
    print("Fall2 er", fall2)
    print("fall1 er", fall)

    b_listi = re.split('[+-]', fall2)
    print(b_listi,"blisti")
    #fall_listi = re.split('[+-]', fall)
    if fall[0] == "+":
        fall = fall[1:]

    if check_index(fall):
        fall_listi = [fall]
    else:
        fall_listi = re.split('[+-]',fall)
        for x in range(len(fall_listi)):
            fall_listi[x] = fall_listi[x].replace(")","")
            fall_listi[x] = fall_listi[x].replace("(","")

    """temp_listi = []
    for x in b_listi:
        for i in range(len(fall_listi)):
            if x in fall_listi[i] and x not in temp_listi:
                fall_listi[i] = fall_listi[i].replace(x, "")
                fall_listi.insert(-1, x)
                temp_listi.append(x)"""



    try:
        fall_listi.remove("")
    except:
        pass

    listi = ["sin", "cos", "tan", "cot"]
    print(fall_listi, "falllistinn")
    for x in range(len(fall_listi)):
        for i in listi:
            if i == fall_listi[x]:
                fall_listi[x] = fall_listi[x] + "(%s)" % fall2

    #print(fall_listi,"þetta er fall listinn")
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
    merki = oll_merkin[1]
    diffrad = []
    dicta = {"sin": "cos", "cos": "-sin"}
    print(fall_listi, "diffrun fær þennan")
    for x in range(len(fall_listi)):
        if "x" in fall_listi[x]:
            i = fall_listi[x]
            sct = check_index(i)
            stadur = i.index("x")
            if sct:
                if sct in i:
                    temp = ""
                    tempx = ""
                    eks = False
                    teljari = 0 #telur hversu margir ) eru komnir
                    teljari1 = -1 #telur hversu margir ( eru komnir
                    teljari2 = i[:-1].count(")")

                    print("Þetta er I í diffrun", i)
                    print("Teljari2 ) er",teljari2)
                    for j in range(len(i)):
                        #print(eks, teljari < teljari1)
                        print(teljari1, teljari)
                        if eks and teljari <= teljari1:
                            print("núna er eks og i[j] er", i[j])
                            if teljari == teljari1 and teljari != 0:
                                pass
                            else:
                                tempx += i[j]
                            #print("went in", tempx)

                        #if i[j] == "(" and eks:

                        if i[j] == "(": #teljari 1 (
                            eks = True
                            teljari1 += 1

                        if i[j] == ")" and eks: #teljari )
                            print("fann )")
                            teljari += 1



                        elif i[j] != "(" and not eks:
                            temp += i[j]
                            #print(temp)

                        print("Þetta er tempx inni í lykkju", tempx)

                        print("Teljari1 ( er", teljari1)

                    if not check_index(tempx) and tempx[-1] == ")": #confirmed rétt if setning og allt inni í henni
                        #print("súper dúper tempx", tempx)
                        tempx = tempx[:-1]

                    """
                    for x in range(teljari-1):
                        tempx+=")"
                    """

                    for key,value in dicta.items():
                        if key == temp:
                            if "+" in temp or "-" in temp:
                                print(tempx, "1")
                                kedja = "(%s)" % str(diffrun(tempx))
                            else:
                                print(tempx, "2")
                                kedja = str(diffrun(tempx))
                            temp = value+"(%s)*" % tempx + kedja
                            print(temp)
                            diffrad.append(temp)
                            #print(diffrad)

                    #teljari = 0


            else:
                print(fall_listi)
                i = fall_listi[x]
                i = i.replace("(", "")
                i = i.replace(")", "")
                print("Þetta er i", i)
                print("lengdin af i",len(i))

                temp_listi1 = i[:stadur]
                temp_listi2 = i[stadur + 1:]

                if len(temp_listi1) != 0 and len(temp_listi2) == 0 and len(i) != 1:
                    # 5x í engu veldi
                    framan = str(int(i[:stadur]))
                    diffrad.append(framan)

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
                    veldi = str(int(i[stadur + 1:]) - 1)
                    if veldi == "1":
                        diffrad.append(framan + "*x")
                    else:
                        diffrad.append(framan + "*x**" + veldi)

                elif stadur == 0 and len(i) == 1:
                    # bara x með engri tölu fyrir framan né veldi.
                    diffrad.append("1")

                print("len(temp_listi1)",len(temp_listi1))
                print("len(temp_listi2)",len(temp_listi2))


        else:
            # 5 í engu veldi
            # gerir ekki neitt, else er bara hérna til að sýna að ef það er ekkert x þá dettur talan bara út
            pass

    diffrad_fall = ""
    print("súper diffrað",diffrad)
    for x in range(len(diffrad)):
        diffrad_fall += merki[x] + diffrad[x]

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

flatarmal1 = flatarmal_falls(fall1, efri1, nedri1)
flatarmal2 = flatarmal_falls(fall2, efri1, nedri1)

print("Flatarmál f(x) og g(x) =", abs(round(flatarmal1 - flatarmal2, 5)))
"""

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
