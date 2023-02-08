dp = {}

def rec(i, j, s1, s2):
    
    if i >= len(s1) or j >= len(s2):
        return 0
    
    if (i, j) in dp:
        return dp[(i,j)]
    
    ans = 0
    ans = max(ans, rec(i+1, j, s1, s2))
    ans = max(ans, rec(i, j+1, s1, s2))
    if s1[i] == s2[j]:
        ans = max(ans, 1 + rec(i+1, j+1, s1, s2))
        
    dp[(i, j)] = ans
    return ans

def solve():
    n, m = map(int, input().split())
    s1 = input()
    s2 = input()
    print(rec(0, 0, s1, s2))

if __name__ == "__main__":
    solve()