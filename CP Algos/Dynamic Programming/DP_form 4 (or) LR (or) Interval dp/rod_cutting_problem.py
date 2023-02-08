dp = {}

def rec(l, r, arr):
    if l+1 == r:
        return 0
    
    if (l,r) in dp:
        return dp[(l ,r)]
    
    ans = 1e9
    for p in range(l+1, r):
        ans = min(ans, (arr[r]-arr[l]) + rec(l, p, arr) + rec(p, r, arr))
        
    dp[(l,r)] = ans
    return ans

def solve():
    n = int(input())
    arr = [0]
    arr.extend(list(map(int, input().split())))
    print(rec(0,n,arr))
    
if __name__ == "__main__":
    solve()