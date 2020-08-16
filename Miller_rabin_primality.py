import random


def primality_test(x, y):                         # Miller-Rabin probabilistic primality test
    p, r = int(x - 1), int(0)
    witness, trust = int(0), int(0)
    while p % 2 == 0:
        r += 1
        p = int(p / 2)
    while trust < y and witness < 2:
        a = random.randint(2, x - 2)
        b = (a ** p) % x
        if b == 1 or b == x-1:
            witness += 1
            continue
        for i in range(1, r):
            b = a**((2**i)*p) % x
            if b == x-1:
                witness += 1
                break
        trust += 1
    if witness >= 2:
        return print(x, "is probably prime")
    return print(x, "is not prime")


def main():
    x = int(input("Enter a number to test for primality (x > 3): "))
    y = int(input("Enter a number of iterations for certainty(x > 1): "))
    primality_test(x, y)


main()
