def sieve(n):
    x = [1 for i in range(n + 1)]
    x[0] = 0
    if n <= 0:
        return x
    x[1] = 0
    p = 2
    while p * p <= n:
        if x[p] == 1:
            for j in range(p * p, n+1, p):
                x[j] = 0
        p += 1
    return x


def main():
    n = int(input())
    p = 0
    for i in sieve(n):
        if i == 1:
            print(p)
        p += 1


main()
