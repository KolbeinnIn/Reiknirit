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
"""

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

