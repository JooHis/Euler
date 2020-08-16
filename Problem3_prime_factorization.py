import time


def file_parser():
    with open("Primes.txt", "r", encoding="utf-8") as file:
        lines = file.read().split()
        primes = list(map(int, lines))
        file.close()
    return primes


factors = []
luvut = file_parser()
x = int(input("Enter a number for prime factorization: "))
start_time = time.time()

while x != 1:
    for i in range(len(luvut)):
        if x % luvut[i] != 0:
            continue
        else:
            while x % luvut[i] == 0:
                factors.append(luvut[i])
                x = x/luvut[i]
    print(x, factors)
    break

if x != 1:
    print("Warning!: Too few primes or remainder is prime!")

print("--- %s seconds ---" % (time.time() - start_time))


