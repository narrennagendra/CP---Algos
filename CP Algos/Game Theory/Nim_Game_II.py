
from sys import stdin

input = stdin.readline

def main():
	n = int(input())
	arr = list(map(int, input().split()))
	ans = 0
	for i in arr: ans ^= (i % 4)
	print("first" if ans else "second")

if __name__  == "__main__":
	for _ in range(int(input())): main()