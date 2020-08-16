import time
import math

def file_parser():
    with open("Primes.txt", "r", encoding="utf-8") as file:
        lines = file.read().split()
        primes = list(map(int, lines))
        file.close()
    return primes


def main():
    primes = file_parser()
    trinum, trisum1, d = int(1), int(1), int(1)

    start_time = time.time()
    while d <= 500:
        d = 1
        factors = {}
        trinum += 1
        trisum1 += trinum
        trisum2 = trisum1
        for p in primes[:10]:
            factors[p] = 0
            while trisum2 % p == 0:
                factors[p] += 1
                trisum2 = trisum2 / p
           # if p > trisum2:
            #    break
        for f in factors.values():
            if f != 0:
                d = (f+1) * d
    print(trinum, trisum1, d, factors)





    print("--- %s seconds ---" % (time.time() - start_time))


main()


