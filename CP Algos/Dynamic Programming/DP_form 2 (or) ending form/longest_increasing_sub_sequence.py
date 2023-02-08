dp = {}

def rec(level, arr):
    # this problem doesnt require any pruning or base case cause its all been handled in the below for loop
    if level in dp:
        return dp[level]
    
    ans = 1
    for i in range(level):
        if arr[i] < arr[level]:
            ans = max(ans, rec(i, arr)+1)
            
    dp[level] = ans
    return ans

def solve():
    
    n = int(input())
    arr = list(map(int, input().split()))
    rec(0, arr)
    
    ans = 0
    for i in range(n):
        ans = max(ans, rec(i , arr))
        
    print(ans)
    
    # this code is for printing the elements but its in reverse order
    """
    ans = 0
    ind = None
    for i in range(n):
        if rec(i, arr) > ans:
            ans = rec(i, arr)
            ind = i
    
    include = [arr[ind]]
    prev = arr[ind]
    x = ans - 1
    for i in range(ind-1,-1,-1):
        if x == 0:
            break
        if rec(i, arr) == x and arr[i] < prev:
            include.append(arr[i])
            prev = arr[i]
            x -= 1
    print(*include)
    """

if __name__ == "__main__":
    solve()