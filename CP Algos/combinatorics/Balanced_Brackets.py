
from sys import stdin
from math import log,floor,ceil,gcd
#from collections import defaultdict as dd
#from bisect import bisect_left as bl,bisect_right as br
#from collections import Counter
#from itertools import groupby


input  =stdin.readline
inp    =lambda: int(stdin.readline())
rs     =lambda: stdin.readline().strip()


def ra(typ) : return list(map(typ, stdin.readline().split()))
def rv(typ) : return map(typ, stdin.readline().split())


#mod = 1000000007


def main():
    for _ in range(inp()):
        s = rs()
        o = {"(","[","{"}
        d = {")":"(","]":"[","}":"{"}
        c = {")","]","{"}
        st = []
        ans = True
        for i in s:
            if i in o:
                st.append(i)
                print(st)
            elif i in c:
                if len(st) and d[i] == st[len(st)-1]:
                    st.pop()
                    print(st)
                else:
                    ans = False
                    break
        print(st)
        if not(ans):
            print("INVALID")
            continue
        elif len(st):
            print("INVALID")
            continue
        else:
            print("VALID")


main()