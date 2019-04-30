# Kolbeinn Ingólfsson
# Lokaverkefni
# ÓÁKVEÐIÐ objective: 100% heildun.
import re

s = "sin(x2+5x)"
m = re.search(".*\(([A-Za-z0-9_+]+)\)", s)
print(m.group(1))

