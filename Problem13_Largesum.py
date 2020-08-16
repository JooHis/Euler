


def main():
    with open("Numbers.txt", "r", encoding="utf-8)") as file:
        lines = file.read().split()
        numbers = list(map(int, lines))
        file.close()

    print(str(sum(numbers))[:10])



main()