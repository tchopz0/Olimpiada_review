import math


def perfect1(x):
    t = 0
    for i in range(1, x - 1):
        if x % i == 0:
            t = t + i
    if t == x:
        return True
    return False


def perfect2(x):
    t = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            t = t + i
    if t == x:
        return True
    return False


def perfect3(x):
    t = 1
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            t = t + i
            if i != x // i:
                t = t + x // i
    if t == x:
        return True
    return False
