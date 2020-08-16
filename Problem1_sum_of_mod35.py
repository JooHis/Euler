import time
start_time = time.time()


def main():
    x = int(0)
    for i in range(1, 1000):
        if i % 5 == 0 or i % 3 == 0:
            x += i
    return x


print(main())
print("--- %s seconds ---" % (time.time() - start_time))