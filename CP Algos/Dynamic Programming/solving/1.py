
from sys import stdin

input = stdin.readline
ii    = lambda: int(input())
ra    = lambda typ : list(map(typ, input().split()))
rv    = lambda typ : map(typ, input().split())
rs    = lambda: input().rstrip()
mod   = 1000000007
mmi = 500000004


def main():
	m, n = rv(int)
	x1 = ((n % mod) * ((n+1) % mod)) % mod
	s1 = (x1 * mmi) % mod
	x2 = ((m % mod) * ((m+1) % mod)) % mod
	s2 = (x2 * mmi) % mod
	ans = (s1 - s2 + m % mod) % mod
	print(ans)


if __name__  == "__main__":
	for _ in range(1): main()