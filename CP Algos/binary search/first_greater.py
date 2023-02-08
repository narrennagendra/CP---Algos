def first_greatest(arr,x):
    l, r = 0, len(arr)-1
    res = -1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] >= x:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res

a = [2,3,3,6,8,10,12]
print(first_greatest(a,13))
        