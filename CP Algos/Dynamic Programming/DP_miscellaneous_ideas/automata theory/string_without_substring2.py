# this is for the specific string t = "0100"
# in this problem we are printing the number of strings possible to generate of length n without having t as substring
# this is an intresting applycation of finite state automata
# use kmp to design finite state automata of any string

dp = {}

def rec(level, state, n):
    if state == 4:
        return 0
    
    if level == n:
        return 1
    
    if (level, state) in dp:
        return dp[(level, state)]
    
    if state == 0:
        ans = rec(level+1, 1, n) + rec(level+1, 0, n)
    elif state == 1:
        ans = rec(level+1, 1, n) + rec(level+1, 2, n)
    elif state == 2:
        ans = rec(level+1, 0, n) + rec(level+1, 3, n)
    else:
        ans = rec(level+1, 4, n) + rec(level+1, 2, n)
        
    dp[(level, state)] = ans
    return ans

def solve():
    n = int(input())
    print(rec(0,0,n))

if __name__ == '__main__':
    solve()