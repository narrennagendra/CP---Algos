# reccursive method

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# itterative method

def main():
    a, b = map(int, input().split())
    while b != 0:
        a, b = b, a % b
    print(a)


main()
