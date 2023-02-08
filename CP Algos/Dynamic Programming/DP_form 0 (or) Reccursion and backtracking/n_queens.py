placed = []

def check(row, col):
    for prow, pcol in enumerate(placed):
        if pcol == col or abs(prow - row) == abs(pcol - col):
            return False
    return True

def nqueens(level, n):
    if level == n:
        return 1
    ans = 0
    for i in range(n):
        if check(level, i):
            placed.append(i)
            ans += nqueens(level+1,n)
            placed.pop()
    
    return ans

def solve():
    n = int(input())
    print(nqueens(0, n))


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
