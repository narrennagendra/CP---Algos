dp = {}

def ways(level,n):
    if level in dp:
        return dp[level]
    if level == n:
        return 1
    ans = 0
    for i in range(1, 4):
        if level + i > n:
            break
        ans += ways(level + i,n)
    dp[level] = ans
    return ans
    

def solve():
    n = int(input())
    if n == 1:
        print(0)
        return
    print(ways(1,n))


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()