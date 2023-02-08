
from sys import stdin

input = stdin.readline
ii    = lambda: int(input())
ra    = lambda typ : list(map(typ, input().split()))
rv    = lambda typ : map(typ, input().split())
rs    = lambda: input().rstrip()
mod   = 1000000007

def solve():
	n = ii()
	coins = ra(int)
	
	dp = [[None for _ in range(n+1)] for _ in range(len(coins)+1)]

	for l in range(len(coins)-1,-1,-1):
		for s in range(n+1):

			if l == len(coins):
				if s == 0:
					dp[l][s] = 1
				else:
					dp[l][s] = 0
				continue

			dp[l][s] = 0
			if dp[l+1][s]:
				dp[l][s] = 1
			if s >= coins[l] and dp[l][s-coins[l]]:
				dp[l][s] = 1
	
	print(dp[0][n])


if __name__  == "__main__":
	for _ in range(1): solve()


# This is a recursive code
# dp = {}

# def rec(level, rem, coins):
# 	if level >= len(coins) or rem < 0:
# 		return False

# 	if rem == 0:
# 		return True
	
# 	if (level, rem) in dp:
# 		return dp[(level, rem)]

# 	ans = rec(level, rem-coins[level], coins) or rec(level+1, rem, coins)
# 	dp[(level, rem)] = ans
# 	return ans

# def solve():
# 	n = ii()
# 	coins = ra(int)
# 	print(rec(0, n, coins))

# if __name__  == "__main__":
# 	for _ in range(1): solve()