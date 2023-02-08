
from sys import stdin

input = stdin.readline

def main():
	n, k = map(int, input().split())
	ans = 0
	p = 0
	for i in range(1,k+1):
		x = ((i/k)**n) - (((i-1)/k)**n)
		ans += (x * i)
	print("%.6f" % ans)

if __name__  == "__main__":
	for _ in range(1): main()