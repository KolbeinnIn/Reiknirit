#Kolbeinn Ingólfsson
#11.1.2019

distances = {"patrek": {"reykjavik": 392, "hallorm":779, "laugar":551, "kirkju":620},
             "reykjavík": {"patrek": 392, "hallorm":570, "laugar":408, "kirkju":251},
             "hallorm": {"reykjavík":570, "patrek":779,  "laugar":227, "kirkju":374},
             "kirkju": {"reykjavík": 251, "patrek":620,  "laugar":372, "hallorm":374},
             "laugar": {"reykjavík":408,  "patrek":551,  "hallorm":227,"kirkju":372}
             }

teljari = 0
for key,value in distances.items():
    for key1, value1 in value.items():
        print(key, "----", end=" ")
        if teljari % 4 == 0:
            print(key1, value1, end=" ")
        else:
            print(key1, value1, end=" ")
        print()

        teljari += 1
