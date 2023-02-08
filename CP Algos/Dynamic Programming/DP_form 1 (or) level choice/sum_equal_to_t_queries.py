dp = {}

def rec(level, arr, sum_left):
    if sum_left == 0:
        #dp[(level, sum_left)] = True
        return True
    
    if level == len(arr) or sum_left < 0:
        return False
    
    if (level, sum_left) in dp:
        return dp[(level, sum_left)]
    
    ans = False
    if rec(level + 1, arr, sum_left):
        ans = True
    elif rec(level + 1, arr, sum_left - arr[level]):
        ans = True
        
    dp[(level, sum_left)] = ans
    return ans
 
def solve():
    _, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        t = int(input())
        print(rec(0, arr, t))
    

if __name__  == "__main__":
    solve()