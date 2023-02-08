dp = {}

def rec(row, col, arr):
    if row == 0 and col == 0:
        return arr[row][col]
    
    if (row, col) in dp:
        return dp[(row, col)]
    
    ans = -1e9 # this is very important
    if row != 0:
        ans = max(ans, arr[row][col]+rec(row-1, col, arr))
    if col != 0:
        ans = max(ans, arr[row][col]+rec(row, col-1, arr))
        
    dp[(row, col)] = ans
    return ans

def solve():
    n, m = map(int, input().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(m):
            rec(i,j,mat)
            
    print(rec(n-1, m-1, mat))
    
if __name__ == '__main__':
    solve()