def rotated(arr):
    n = len(arr)
    l,r = 0,n-1
    ans = -1
    while l <= r:
        m = l + (r - l)//2
        if arr[m] <= arr[n-1]:
            ans = arr[m]
            r = m - 1
        else:
            l = m + 1
    return ans

print(rotated([6,7,9,15,19,2,3]))