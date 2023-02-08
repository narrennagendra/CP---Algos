def main():
    n = int(input())  # no. of prime factors [ie. n0. of a ^ n]
    ans = 0
    for _ in range(n):
        a, n = map(int, input().split())
        ans *= n+1
    print(ans)


main()

# if the answer is large and need to print it in 10^9+7
mod = (10 ** 9) + 7


def main():
    n = int(input())  # no. of prime factors [ie. n0. of a ^ n]
    ans = 0
    for _ in range(n):
        a, n = map(int, input().split())
        ans *= n+1 % mod
    print(ans % mod)


main()
