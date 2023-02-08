mod = 1 ** 9 + 7
def vbrac(n):
    x = [1]
    for i in range(1,n+1):
        ans = 0
        for j in range(i):
            ans = (ans + x[j] * x[i-j-1]) % mod
        x.append(ans)
    return x.pop()