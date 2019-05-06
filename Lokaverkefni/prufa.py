import re

asd = "-sin+cos"

print(re.sub(r'[+-]', "", asd))
