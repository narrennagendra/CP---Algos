def matmul(a, b):
    x = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                x[i][j] += a[i][k] * b[k][j]
    return x


def main():
    n, b = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    x = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    while b:
        if b % 2 == 1:
            x = matmul(x, a)
            b -= 1
        else:  # no need to take else
            a = matmul(a, a)
            b //= 2
    for i in x:
        print(*i)


main()
