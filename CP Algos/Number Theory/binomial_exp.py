def power(a, n):
    res = 1
    while n:
        if n & 1 == 1:
            res *= a
            n -= 1
        else: # we dont need to give any else statement over here
            n >>= 1
            a *= a
    return res

def power_mod(a, n, p):
    res = 1
    while n:
        if n & 1 == 1:
            res = (res * a) % p
            n -= 1
        else:
            n >>= 1
            a = (a * a) % p
    return res