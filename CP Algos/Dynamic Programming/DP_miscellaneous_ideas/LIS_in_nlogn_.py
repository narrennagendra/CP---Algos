from bisect import bisect_left
def solve():
    n = int(input())
    arr = list(map(int, input().split())) 
    
    inserted = []  # this array is to print the subsequence
    dp = []
    for i in arr:
        if len(dp) == 0 or dp[-1] < i:
            dp.append(i)
            inserted.append(len(dp))
        else:
            ind = bisect_left(dp, i)
            dp[ind] = i
            inserted.append(ind+1)
                
    print(len(dp))
    
    # for printing the subsequnce reffer the below code
    """
    sub_arr = []
    pointer = len(dp)
    for i in range(n-1,-1,-1):
        if inserted[i] == pointer:
            sub_arr.append(arr[i])
            i -= 1
    print(sub_arr[::-1])
    """

if __name__ == '__main__':
    solve()