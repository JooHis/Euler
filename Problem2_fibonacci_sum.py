import time
start_time = time.time()


def main():
    x_1, x_2 = int(1), int(1)
    fibonacci_sum = int(0)
    while x_2 < 4000000:
        if x_2 % 2 == 0:
            fibonacci_sum += x_2
        x_2 += x_1
        x_1 = x_2 - x_1
    return fibonacci_sum


print(main())
print("--- %s seconds ---" % (time.time() - start_time))
