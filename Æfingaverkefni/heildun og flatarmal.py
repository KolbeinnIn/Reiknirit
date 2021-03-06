# Kolbeinn Ingólfsson
# Heildun og flatarmál

import re


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


fall1 = input("Sláðu inn fall f(x): ")
fall2 = input("Sláðu inn fall g(x): ")
efri1 = float(input("Sláðu inn x fyrir efri mörk: "))
nedri1 = float(input("Sláðu inn x fyrir neðri mörk: "))
print("--------------------------------")

flatarmal1 = flatarmal_falls(fall1, efri1, nedri1)
flatarmal2 = flatarmal_falls(fall2, efri1, nedri1)

print("Flatarmál f(x) og g(x) =", abs(round(flatarmal1 - flatarmal2, 5)))
