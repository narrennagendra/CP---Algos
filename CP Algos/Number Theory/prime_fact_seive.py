def prime_fact(n):
    x = [-1 for i in range(n+1)]
    for i in range(2,n+1):
        if i*i > n:
            break
        if x[i] == -1:
            x[i] = i
            for j in range(i*i,n+1,i):
                if x[j] == -1:
                    x[j] = i
    return x

def main():
    max = 10 ** 7
    ans = prime_fact(max)
    for _ in range(int(input())):
        n = int(input())
        f = []
        while n > 1:
            f.append(ans[n])
            n //= ans[n]
        print(*f)
main()