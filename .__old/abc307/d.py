N = int(input())
S = input()

import re

print(re.findall("(?<=\().+?(?=\))", S))

