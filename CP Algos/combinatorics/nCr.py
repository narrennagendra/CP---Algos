mod = 10 ** 9 + 7
f = [1, 1]


def fact():
    for i in range(2, 10 ** 6 + 1):
        f.append((f[i-1] * i) % mod)


fact()


def ncr(n, r):
    ans = (f[n] * pow(f[r], mod-2, mod)) % mod
    ans = (ans * pow(f[n-r], mod-2, mod)) % mod
    return ans
