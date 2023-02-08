
from sys import stdin
from math import log,floor,ceil,gcd
from collections import defaultdict as dd
#from bisect import bisect_left as bl,bisect_right as br


input  =stdin.readline
inp    =lambda: int(stdin.readline())
rs     =lambda: stdin.readline().strip()


def ra(typ) : return list(map(typ, stdin.readline().split()))
def rv(typ) : return map(typ, stdin.readline().split())


mod = 1000000007
def matmul(a, b):
    x = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                x[i][j] += (a[i][k] * b[k][j])
    return x
def matpow(a, n):
    x = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
    while n:
        if n % 2 == 1:
            x = matmul(x, a)
            n -= 1
        else:
            a = matmul(a, a)
            n //= 2
    return x

def main():
    for _ in range(inp()):
        A,B,N = rv(int) # here A is the F0 and B is F1 and N is the nth term of the deries we need to find
        x = [[0, 1], [1, 1]]  # this is the magic matric of the reccursive relation
        if N == 0:
            print(A)
        else:
            ans = matpow(x, N)
            print((A*ans[0][0]) + (B*ans[1][0]))


main()
