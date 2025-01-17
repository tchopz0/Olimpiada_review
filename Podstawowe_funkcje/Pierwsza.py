import math
import re

def primal1(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(2, math.isqrt(x) + 1, 2):
        if x % 1 == 0:
            return False
    return True


# the best efficiency
def primal2(x):
    if x < 2:
        return False
    if x in (2, 3, 5):
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    for i in range(6, math.isqrt(x) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True


# silly metoda na pierwsza liczbe z yt halloween od taty
def primal3(x):
    return not re.match(r'^.?$|^(..+?)\1+$', '1' * x)


n = 58259837
print(primal1(n))
print(primal2(n))
print(primal3(n))

