dp = {}

def rec(level, taken, x, n, last, l, seter):
    if level == n:
        return 1
    
    if (level, taken) in dp:
        return dp[(level, taken)]
    
    ans = 0
    if taken == x and level >= l:
        ans += rec(level+1, last, x, n, last, l, seter)
    else:
        ans += rec(level+1, (taken<<1|1)&seter, x, n, last, l, seter)
        ans += rec(level+1, (taken<<1|0)&seter, x, n, last, l, seter)
        
    dp[(level, taken)] = ans
    return ans

def solve():
    n = int(input())
    t = input()
    x = int(t[:-1], 2)
    l = len(t) - 1
    seter = int("1"*l, 2)
    last = int(t, 2) ^ 1
    print(rec(0, 0, x, n, last, l, seter))

if __name__ == '__main__':
    solve()