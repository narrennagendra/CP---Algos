
from sys import stdin
from collections import deque

input = stdin.readline

x8 = [-1, -1, 0, 1, 1, 1, 0, -1]
y8 = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(mat, i, j):
	q = deque([(i, j)])
	c = 0
	while len(q):
		ni, nj = q.popleft()
		c += 1
		mat[ni][nj] = 0
		for x, y in zip(x8, y8):
			if 0 <= ni+x < len(mat) and 0 <= nj+y < len(mat[0]) and mat[ni+x][nj+y]:
				mat[ni+x][nj+y] = 0
				q.append((ni+x,nj+y))
	return c

def main():
	n, m = map(int, input().split())
	mat = []
	for _ in range(n):
		mat.append(list(map(int, input().split())))
	
	ans = 0
	for i in range(n):
		for j in range(m):
			if mat[i][j]:
				ans = max(ans, bfs(mat, i, j))
	
	print(ans)

if __name__  == "__main__":
	for _ in range(1): main()