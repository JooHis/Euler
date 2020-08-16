def check_division(x):
    for i in range(1, 21):
        if x % i != 0:
            return True
    return False


def main():
    x = int(5040)
    while check_division(x):
        x += 5040
    print(x)


main()