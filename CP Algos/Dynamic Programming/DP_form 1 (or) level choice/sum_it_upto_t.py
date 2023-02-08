dp = {}

def rec(level, sum_taken, arr, t):
    
    if sum_taken == t:
        #dp[(level, sum_taken)] = True
        return True
    
    if level == len(arr) or sum_taken > t:
        return False
    
    if (level, sum_taken) in dp:
        return dp[level][sum_taken]
    
    ans = False
    if rec(level + 1, sum_taken, arr, t):
        ans = True
    elif rec(level + 1, sum_taken + arr[level], arr, t):
        ans = True
        
    dp[(level, sum_taken)] = ans
    return ans
        
def solve():
    _, t = map(int, input().split())
    arr = list(map(int, input().split()))
    print(rec(0, 0, arr, t))
    
if __name__ == "__main__":
    solve()