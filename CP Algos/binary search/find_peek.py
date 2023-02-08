def find_peek(a):
    le = len(a)
    l,r = 0, le - 1
    ans = a[0]
    while l <= r:
        m = l + (r - l) // 2
        if a[m] > ans:
            ans = a[m]
            l = m + 1
        else:
            r = m - 1
    return ans

print(find_peek([5,1]))