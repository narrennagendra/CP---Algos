
from sys import stdin

input = stdin.readline

def dfs(visited, x, y, r, c, count):
	count += 1
	visited[x][y] = count
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			if 0 <= i < r and 0 <= j < c and not visited[i][j]:
				dfs(visited, i, j, r, c,count)

def main():
	r, c = map(int, input().split())
	visited = [[0 for _ in range(c)] for _ in range(c)]
	dfs(visited, 0, 0, r, c, 0)
	for i in visited:
		print(*i)

if __name__  == "__main__":
	for _ in range(1): main()


