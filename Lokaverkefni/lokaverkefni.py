import re
import math


def master(func, args=""):  # hér er fall til að einfalda kóðann aðeins þegar notandi velur hvað hann vill gera.
    # fallið tekur inn annað fall sem notandi valdi og það sem hann vill setja í fallið (parametra) og kallar í það
    # Sjá kóða og comments alveg neðst í skjalinu.
    if args != "":
        return func(args)


def merkin(fall):
    # Fallið merkin finnur + og - í fallinu og setur það í lista í réttri röð
    # listinn er notaður seinna til að bæta því inn í lokaútkomuna

    if fall[0] != "-":  # til að halda jafn mörgum merkjum og eru liðir í dæminu bætist + fyrir framan ef það er ekki - nú þegar
        fall = "+" + fall

    merki = []
    for x in fall:
        if x == "+" or x == "-":
            merki.append(x)

    fall2 = ""
    a1 = 0
    a2 = 0
    # við viljum fá innstu tvo svigana, hér telur for lykkja frá vinstri til að finna innsta svigann sem lokar
    for x in range(len(fall)):
        if fall[x] == ")":
            a1 = x + 1
            break
    # væri líka hægt að gera for x in range(len(fall[::-1)): en þetta er læsilegra
    for x in range(len(fall), 0,
                   -1):  # hér fer for lykkjan í öfuga átt til að finna fyrsta svigann sem opnark, talinn frá hægri
        if fall[x - 1] == "(":
            a2 = x - 1
            break
    # cos(cos(cos(x)))
    # finnur þá svigana sem eru inni í gæsalöppum
    # cos(cos(cos"("x")"))

    fall2 = fall[a2 + 1:a1 - 1]
    # fall2 er þá það sem er í innstu svigunum, notað fyrir keðjuregluna

    # hér tökum við plúsinn af sem við bættum við aðeins fyrr vegna þess að hann er kominn í listann
    # og þarf ekki að vera í fallinu lengur
    if fall[0] == "+":
        fall = fall[1:]

    if check_index(fall):  # check_index fallið kíkir hvort sin,cos,tan og framveigis er í fallinu. og setur það í lista
        fall_listi = [fall]
    else:  # ef það er ekki sin eða cos og svoleiðis er fallinu splittað í marga liði með + og -
        fall_listi = re.split('[+-]',
                              fall)  # einfaldara að nota re.split frekar en built-in .split vegna þess að re.split getur splittað á fleiri en einum staf, (+ og -)
        for x in range(len(fall_listi)):
            fall_listi[x] = fall_listi[x].replace(")", "")  # óþarfa svigar teknir
            fall_listi[x] = fall_listi[x].replace("(", "")

    try:
        fall_listi.remove(
            "")  # bætist oft tómt stak í listann, það er fjarlægt hér, það kemur error ef það er ekki, þess vegna try og except
    except:
        pass

    listi = ["sin", "cos", "tan", "cot", "ln"]  # listinn yfir föllum sem þarf að kíkja á
    for x in range(len(fall_listi)):
        for i in listi:
            if i == fall_listi[x]:  # finnum hvar sin,cos,tan... er í listanum og bætum því sem var í innsta sviganum þar inn.
                fall_listi[x] = fall_listi[x] + "(%s)" % fall2

    # return lista með föllum í sem þarf að diffra og merkjunum.
    return fall_listi, merki


def check_index(string):
    # fall sem finnur hvort sin,cos,tan,cot og ln er í dæminu og skilar staðsetningu þess, ef það finnur ekki, returnar það False
    listi = ["sin", "cos", "tan", "cot", "ln"]
    for x in listi:
        if x in string:
            return x
    return False


def u_v(fall):
    # kallað er í þetta fall ef fallið "diffrun" finnur "/" eða "*" í fallinu.
    if "/" in fall:
        u_v_listi = fall.split('/')  # splittar í u og v, u fyrir ofan strik, v fyrir neðan

        u = u_v_listi[0]  # u eða f(x)
        v = u_v_listi[1]  # v eða g(x)

        du = diffrun(u)  # diffrað u eða f'(x)
        dv = diffrun(v)  # diffrað v eða g'(x)

        bandstrik = ""
        for x in range(len("%s*%s - %s*%s" % (du, v, u, dv)) + 1):
            bandstrik += "-"

        formula = "%s*%s) - %s*(%s)\n%s\n(%s)^2" % (du, v, u, dv, bandstrik, v)

    elif "*" in fall:
        u_v_listi = fall.split('*')  # splittar í u og v, alveg eins og hér fyrir ofan nema bara margföldun
        u = u_v_listi[0]
        v = u_v_listi[1]

        du = diffrun(u)
        dv = diffrun(v)
        formula = "%s*%s) + %s*(%s" % (du, v, u, dv)
    else:
        formula = ""
    return formula


def diffrun(fall):
    oll_merkin = merkin(fall)
    fall_listi = oll_merkin[0]
    merki = oll_merkin[1]
    diffrad = []
    diffrad_uv = []
    dicta = {"sin": "cos", "cos": "-sin", "tan": "sec2", "cot": "-csc2", "ln": "1/"}
    for x in range(len(fall_listi)):
        if "x" in fall_listi[x]:
            if "/" in fall_listi[x] or "*" in fall_listi[x]:
                diffrad.append(u_v(fall_listi[x]))
            else:
                i = fall_listi[x]
                sct = check_index(i)  # athugar hvort það er sin cos tan.... í stakinu
                if sct:  # ef það er.
                    if sct in i:
                        temp = ""
                        tempx = ""
                        eks = False  # eks er "x" nema skrifað öðruvísi, eks verður true þegar það finnur sviga sem opnast,
                        # þetta er leið til að finna það sem er inni í sviganum
                        # þessir teljarar passa uppá að það lokast jafn margir svigar og opnast, talað er um það vandamál í dagbókinni undir 03.05
                        teljari = 0  # telur hversu margir ) eru komnir
                        teljari1 = -1  # telur hversu margir ( eru komnir

                        for j in range(len(i)):
                            if eks and teljari <= teljari1:
                                if teljari == teljari1 and teljari != 0:
                                    pass
                                else:
                                    tempx += i[j]

                            if i[j] == "(":  # teljari 1 (
                                eks = True
                                teljari1 += 1

                            if i[j] == ")" and eks:  # teljari )
                                teljari += 1

                            elif i[j] != "(" and not eks:
                                temp += i[j]

                        if not check_index(tempx) and tempx[-1] == ")":
                            tempx = tempx[:-1]

                        for key, value in dicta.items():
                            temp_temp = re.sub(r'[+-]', "", temp)  # það eru engir + né - í keys í dictionary-inu
                            # þannig þeir eru fjarlægðir hér án þess að breyta temp-inu sjálfu
                            if key == temp_temp:
                                if "+" in temp_temp or "-" in temp_temp:
                                    kedja = "(%s)" % str(diffrun(tempx))  # endurkvæmni
                                else:
                                    temp_diffrun = diffrun(tempx)
                                    if temp_diffrun != "":
                                        kedja = "(%s)" % temp_diffrun  # endurkvæmni
                                    else:
                                        kedja = ""

                                if "/" in value:  # þetta er bara hér ef ln(x2) er sett inn, þá er það diffrað sem 1/x2 og þá er komið "/"
                                    # útkoman er þá (2x)1/x2 í stað 1/x2(2x)
                                    if kedja != "":  # ef kedjureglan var notuð
                                        temp = "(%s)" % (kedja) + value + tempx
                                    else:  # ef keðjureglan var ekki notuð, t.d. í ln(x) væri rétta svarið 1/x en ekki ()1/x
                                        temp = value + tempx  # sviginn er ekki hérna vegna þess að það yrði ekkert inni í honum
                                else:
                                    temp = value + "(%s)" % tempx + kedja

                                diffrad.append(temp)  # diffraða dæmið bætist í listann

                else:  # ef það er ekki sin cos tan....
                    # ef það eru óþarfa svigar þá eru þeir teknir í burtu
                    i = fall_listi[x]
                    i = i.replace("(", "")
                    i = i.replace(")", "")

                    stadur = i.index("x")  # staðsetningin á x
                    temp_listi1 = i[:stadur]  # allt fyrir framan x.
                    temp_listi2 = i[stadur + 1:]  # allt fyrir aftan x (veldi)
                    if len(temp_listi1) != 0 and len(temp_listi2) == 0 and len(i) != 1:
                        # ef það er eitthvað fyrir framan x og ekkert fyrir aftan.
                        # forritið fer í þessa if setningu ef það er tala fyrir framan x í engu veldi. t.d. 5x
                        framan = str(int(i[:stadur]))
                        diffrad.append(framan)

                    if stadur == 0 and len(i) >= 2:
                        # if stadur == 0 gerir það sama og len(temp_listi1) != 0, bæði athugar hvort það er eitthvað fyrir framan x,
                        # x er alltaf 1 af len(i) þannig ef len(i) >= 2 þá er veldi,
                        # ástæðan fyrir stærra en er vegna þess að veldið á að geta verið stærra en 9, þá er len(i) 3

                        # forritið fer í þessa if setningu ef það er EKKI tala fyrir framan x í veldi. x2, x3, x27
                        framan = int(i[stadur + 1:])  # það sem á að fara fyrir framan x (veldið)
                        veldi = framan - 1  # veldið eftir diffrun, þess vegna -1
                        if veldi != 0:  # ef veldið er EKKI 0
                            if veldi == 1:  # ef veldið er 1 þá bætist 2 framaná og bara *x aftaná
                                diffrad.append(str(framan) + "*x")  # basically bara x2 verður 2x

                            elif veldi > 1:  # en ef það stærra en 1 bætist það aftaná
                                diffrad.append(str(framan) + "*x**" + str(veldi))
                        else:
                            diffrad.append(str(framan) + "*x**" + str(veldi))

                    elif stadur != 0 and len(i) > 2:
                        # forritið fer í þessa if setningu ef það ER tala fyrir framan x OG í veldi. 2x2, 6x3, 157x27
                        framan = str(int(i[:stadur]) * (int(i[stadur + 1:])))
                        veldi = str(int(i[stadur + 1:]) - 1)
                        if veldi == "1":
                            diffrad.append(framan + "*x")
                        else:
                            diffrad.append(framan + "*x**" + veldi)

        else:
            # tala í engu veldi
            # gerir ekki neitt, else er bara hérna til að sýna að ef það er ekkert x þá dettur talan bara út
            pass

    # Hér byrjar forritið að úitfæra loka lausnina á fallegan máta, -cos(x3)(3x2) í stað -cos(x**3)*3*x**2
    diffrad_fall = ""
    for x in range(len(diffrad)):
        diffrad_fall += merki[x] + diffrad[x]
    listi = ["*"]
    pretty_diffrad = diffrad_fall

    if diffrad_fall != "":  # ef að það er eitthvað í fallinu
        if check_index(diffrad_fall):  # kíkja hvort það er sin, cos, tan og slíkt í fallinu
            if diffrad_fall[-1] == "*":
                # vegna keðjureglunnar bætist við margföldunarmerki aftast þótt að það er ekkert aftast.
                # Dæmi: sin(x) verður cos(x)*1 en *1 gerir ekki neitt þannig ásinn bætist ekki við aftast en margföldunarmerkið verður samt.
                diffrad_fall = diffrad_fall[:-1]  # hér fer seinasta stjarnan ef hún er til staðar
            kedjureglan = False
            try:
                kedjureglan = diffrad_fall.index(
                    ")*")  # kíkja hvar diffraða fallið endar og keðjureglan byrjar, cos(x2)*(2x)
            except:  # ef .index() built-in fallið finnur það ekki kemur error, þetta try og expect kemur í veg fyrir errorinn
                pass

            if kedjureglan:  # ef .index fann ")*"
                temp1 = diffrad_fall[:kedjureglan + 1]
                temp2 = diffrad_fall[kedjureglan + 2:]
                temp1 = temp1.replace("*", "")
                temp2 = temp2.replace("*", "")
                nytt = "%s(%s)" % (temp1,
                                   temp2)  # hér bætist sviginn utan um það sem diffraðist inni í falli (keðjureglan), talað er um það í dagbókinni líka
                pretty_diffrad = nytt

        else:  # ef það er ekki fall inni í falli (sin, cos, tan og það), er engin keðjuregla þannig það er bara hægt að taka * alveg
            pretty_diffrad = diffrad_fall.replace("*", "")

    try:
        # try og except er hér vegna þess að ef eitthvað annað fer úrskeðis í forritinu (eins og gerist á meðan maður forritar)
        # þá endaði errorinn mjög oft hér vegna þess að pretty_diffrad væri tómt, einnig er það hér útaf user error
        if pretty_diffrad[0] == "+":
            pretty_diffrad = pretty_diffrad[1:]
        elif pretty_diffrad[:2] == "--":
            pretty_diffrad = pretty_diffrad[2:]
    except:
        pass

    # skilar loka útkomu
    return pretty_diffrad


# heildun fallið returnar heilduðu falli EKKI pretty printað, dæmi: 2*x**2 væri 2x2 pretty printað, þetta er bara til að geta notað eval() fallið.
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
                rounded = str((int(x[stadur + 1]) + 1))
                framan = str(rounded)
                veldi = str(int(x[stadur + 1]) + 1)
                heildad.append("(x)**" + veldi + "/"+ framan)

            elif stadur != 0 and len(x) > 2:
                framan = str(int(x[:stadur])) + "/" + str((int(x[stadur + 1:]) + 1))
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

    return "Rúmmál: " + str(round(math.pi * (heilda(fall)),5))


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
        flatarmal1 = ""
        flatarmal2 = ""
        try:
            flatarmal1 = round(abs(eval(nytt_fall_b1) - eval(nytt_fall_a1)), 5)
            flatarmal2 = round(abs(eval(nytt_fall_b2) - eval(nytt_fall_a2)), 5)
        except:
            pass

        #print(flatarmal1,flatarmal2)
        if rummal_YN:
            return abs(float(flatarmal1))

        else:
            return "Flatarmál á milli f(x) og g(x) er %s" % abs(flatarmal1 - flatarmal2)

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
    print("ATH! veldi eru skrifuð sem tala eftir x, x í veldinu 2 væri x2")
    print("Útaf þessu er ekki hægt að setja veldi í - tölu, forritið tekur því sem venjulegri tölu t.d. x-2")
    print("Vinsamlegast einfaldið föll, þetta er diffur og heildunar reiknivél ekki einföldunarvél.")
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
        fall = (fall1, fall2, efri, nedri)  # inputtar sem tuple

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
        if utkoma == " ":  # ef notandi vildi endilega heilda töluna 0 þá auðvitað kemur ekkert út
            print("C")
        else:  # ef notandi vildi heilda tölu sem er ekki 0
            print(master(func, fall) + " + C")
    else:
        print(master(func, fall))
    print()
