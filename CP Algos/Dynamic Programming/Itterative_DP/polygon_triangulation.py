
from sys import stdin
from math import sin, inf

input = stdin.readline
ii    = lambda: int(input())
ra    = lambda typ : list(map(typ, input().split()))
rv    = lambda typ : map(typ, input().split())
rs    = lambda: input().rstrip()
mod   = 1000000007

def cost(x, y):
	dist = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
	return sin(dist)

def solve():
	n = ii()
	cord = []
	for _ in range(n): cord.append(ra(int))
	dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
	for len in range(3,n+1):
		for l in range(1, n-len+2):
			r = l + len - 1
			if len == 3:
				return 0
			ans = inf
			for x in range(l+1, r):
				if x == l+1:
					ans = min(ans, cost(l+1, r)+dp[l+1][r])
				elif x == r-1:
					ans = min(ans, cost(l, r-1)+dp[l][r-1])
				else:
					ans = min(ans, cost(l,x)+cost(x, r) + dp[l][x] + dp[x][r])
			dp[l][r] = ans
			
	print(dp[1][n])


if __name__  == "__main__":
	for _ in range(1): solve()

# This is the reccursive approach
# dp = {}

# def cost(x, y):
# 	dist = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
# 	return sin(dist)

# def rec(l, r):
# 	if r - l + 1 < 3:
# 		return 0

# 	if (l, r) in dp:
# 		return dp[(l, r)]

# 	ans = None
# 	for x in range(l+1, r):
# 		t_cost = cost(cord[l], cord[x]) + cost(cord[r], cord[x]) + rec(l, x) + rec(x, r)

# 		if ans is None:
# 			ans = t_cost
# 		else:
# 			ans = min(ans, t_cost)

# 	dp[(l, r)] = ans
# 	return ans

# if __name__  == "__main__":
# 	for _ in range(1):
# 		n = ii()
# 		cord = []
# 		for _ in range(n): cord.append(ra(int))