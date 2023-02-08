def check(s):
    opening, closing = 0, 0
    for i in s:
        if i == "(":
            opening += 1
        elif i == ")":
            closing += 1
        if closing > opening:
            return False
    if opening == closing:
        return True
    return False


def main():
    ans = check(input())
    print("valid" if ans else "invalid")


main()
