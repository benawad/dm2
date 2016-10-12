from itertools import product
from string import ascii_lowercase

def valid(s):
    z = False
    for i in s:
        if i == 'z':
            z = True
        if z and i == 'a':
            return False
    return True

n = 5

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = n)]

perms = 0

for k in keywords:
    if valid(k):
        perms += 1

print(perms)
