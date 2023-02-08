def is_suare(n):
    l,r = 1,n
    while l <= r:
        m = l + (r-l) // 2
        res = m ** 2
        if res == n:
            return True
        elif res < n:
            l = m+1
        else:
            r = m - 1
    return False

# more optimised version of that is
def is_suare(n):
    if n < 2:
        return True
    l,r = 2,n//2 + 1
    while l <= r:
        m = l + (r-l) // 2
        res = m ** 2
        if res == n:
            return True
        elif res < n:
            l = m+1
        else:
            r = m - 1
    return False

x = 9
print(is_suare(x))
