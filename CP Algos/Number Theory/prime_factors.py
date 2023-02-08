def primeFactors(n):
    for i in range(2,round(n**0.5)+1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(f"{i} ^ {cnt}")
    if n > 1:
        print(f"{n} ^ 1")


def main():
    primeFactors(7)


main()
