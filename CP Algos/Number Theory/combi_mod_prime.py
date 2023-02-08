# given q queries of type N K , calculate C(N, K) % P, where P > N and P is a prime number(if N > P we would use lucas theorm)

# note that 10^9+7 is a prime number

# C(N, K) = (N!)/(K! * (N-K)!)
# C(N, K) % P = (N!%P)/((K!%P)*((N-K)!%P))

def main():
    P = (10 ** 9) + 7
    F = [0 for i in range(1000001)]
    F[0], F[1] = 1, 1
    for i in range(2, 1000001):
        F[i] = (F[i-1] * i) % P
    q = int(input())
    for _ in range(q):
        N, K = map(int, input().split())
        if K > N:
            print(0)
        else:
            ans = F[N]
            ans *= (F[K] ** (P-2)) % P  # inverse modulo
            ans *= (F[N-K] ** (P-2)) % P  # inverse modulo


main()
