# if all transition states are winning then current player is loosing
# if any lossing state then current player is winning

dp = {}

def rec(x):
    if x == 0:
        return 0
    
    if x in dp:
        return dp[x]
    
    ans = 0
    m = 1
    while m <= x:
        if rec(x-m) == 0:
            ans = 1
            break
        m <<= 1
    
    dp[x] = ans
    return ans
        
def solve():
    n = int(input())
    # print(rec(n))
    if n % 3 == 0:
        print(1)
    else:
        print(0)
    
if __name__ == "__main__":
    solve()