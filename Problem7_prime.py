from math import sqrt, floor


def main():
    primes, candidate = int(2), int(1)

    while primes != 10001:
        candidate += 2
        if str(candidate)[-1:] in "13579":
            for i in range(2, floor(sqrt(candidate))+1):
                if candidate % i == 0:
                    break
                elif i == floor(sqrt(candidate)):
                    primes += 1
    print(candidate, primes)


main()