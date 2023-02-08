
from sys import stdin

input = stdin.readline
ii    = lambda: int(input())
ra    = lambda typ : list(map(typ, input().split()))
rv    = lambda typ : map(typ, input().split())
rs    = lambda: input().rstrip()
mod   = 1000000007

def solve():
	n = ii()
	arr = ra(int)
	dp = [None for _ in range(n)]
	ans = -1e9
	for i in range(n):
		if i == 0:
			dp[i] = arr[i]
		else:
			dp[i] = max(dp[i-1]+arr[i], arr[i])

		ans = max(ans, dp[i])

	print(ans)
	
	# approach with O(1) space complexity
	# ans = arr[0]
	# prev = arr[0]
	# for i in range(1, n):
	# 	cal = max(arr[i], arr[i]+prev)
	# 	prev = cal
	# 	ans = max(ans, cal)
	# print(ans)

if __name__  == "__main__":
	for _ in range(1): solve()