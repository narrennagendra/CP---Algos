def rec(i, j, k, s1, s2, s3, dp):
    if i >= len(s1) or j >= len(s2) or k >= len(s3):
        return 0
    
    if (i, j, k) in dp:
        return dp[(i, j, k)]
    
    ans = 0
    ans = max(ans, rec(i+1, j, k, s1, s2, s3, dp))
    ans = max(ans, rec(i, j+1, k, s1, s2, s3, dp))
    ans = max(ans, rec(i, j, k+1, s1, s2, s3, dp))
    if s1[i] == s2[j] == s3[k]:
        ans = max(ans, 1+rec(i+1, j+1, k+1, s1, s2, s3, dp))
        
    dp[(i, j, k)] = ans
    return ans

def solve():
    dp = {}
    s1, s2, s3 = input().split()
    print(rec(0, 0, 0, s1, s2, s3, dp))
    

if __name__ == "__main__":
    solve()