# Given a two piles A and B which contains some number of stones
# there are two possible moves
# 1) we can taken any number of stones from either A or B
# 2) we can take any number of equal stones from A and B


from sys import stdin

input = stdin.readline
ii    = lambda: int(input())
ra    = lambda typ : list(map(typ, input().split()))
rv    = lambda typ : map(typ, input().split())
rs    = lambda: input().rstrip()
mod   = 1000000007

def solve():
    a, b = rv(int)
    dp = [[None for _ in range(b+1)] for _ in range(a+1)]

    for x in range(a+1):
        for y in range(b+1):
            
            if x == 0 and y == 0:
                dp[x][y] = 0
                
            ans = 0
            for i in range(1, x+1):
                if dp[x-i][ y] == 0:
                    ans = 1
                    break
            if ans != 1:
                for i in range(1, y+1):
                    if dp[x][y-i] == 0:
                        ans = 1
                        break
    
            if ans != 1:
                for i in range(1, min(y, x)+1):
                    if dp[x-i][y-i] == 0:
                        ans = 1
                        break
            
            dp[x][y] = ans
            
    print("Player 1" if dp[a][b] else "Player 2")
                

if __name__  == "__main__":
	for _ in range(1): solve()	

# this is a reccursive code
# dp = {}

# def rec(x, y):
#     if x == 0 and y == 0:
#         return 0
    
#     if (x, y) in dp:
#         return dp[(x, y)]
    
#     ans = 0
#     for i in range(1, x+1):
#         if rec(x-i, y) == 0:
#             ans = 1
#             break
    
#     if ans != 1:
#         for i in range(1, y+1):
#             if rec(x, y-i) == 0:
#                 ans = 1
#                 break
    
#     if ans != 1:
#         for i in range(1, min(y, x)+1):
#             if rec(x-i, y-i) == 0:
#                 ans = 1
#                 break
            
#     dp[(x, y)] = ans
#     return ans
        
# def solve():
#     a, b = 1,2
#     if rec(a, b):
#         print("player 1")
#     else:
#         print("player 2")

# if __name__  == "__main__":
# 	for _ in range(1): solve()