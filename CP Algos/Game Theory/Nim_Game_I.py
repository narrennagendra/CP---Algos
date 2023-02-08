
from sys import stdin

input = stdin.readline

def main():
	n = int(input())
	arr = list(map(int, input().split()))
	x = 0
	for i in arr: x ^= i
	print("first" if x else "second")

if __name__  == "__main__":
	for _ in range(int(input())): main()