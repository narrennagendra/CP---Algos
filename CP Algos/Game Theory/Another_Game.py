
from sys import stdin

input = stdin.readline

def main():
	n = int(input())
	arr = list(map(int, input().split()))
	x = [1 if i % 2 == 0 else 0 for i in arr ]
	print("second" if all(x) else "first")

if __name__  == "__main__":
	for _ in range(int(input())): main()