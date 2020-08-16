from math import sqrt, floor


def main():
    primes = [2, 3]
    for i in range(5, 2000001, 2):
        if str(i)[-1:] in "13579":
            for j in range(2, floor(sqrt(i))+1):
                if i % j == 0:
                    break
                elif j == floor(sqrt(i)):
                    primes.append(i)
    print(sum(primes))


main()