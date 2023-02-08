dp = {}

def rec(level, taken, l, n):
    if taken >= l:
        return 0
    
    if level == n:
        return 1
    
    if (level, taken) in dp:
        return dp[(level, taken)]
    
    ans = rec(level+1, taken, l, n) + rec(level+1, taken+1, l, n)
    
    dp[(level, taken)] = ans
    return ans

def solve():
    n = int(input())
    t = input()
    print(rec(0,0,len(t),n))
    
if __name__ == '__main__':
    solve()