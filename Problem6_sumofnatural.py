def main():
    numbers = []
    numbers_square = []

    for i in range(1, 101):
        numbers.append(i)
    for j in range(1, len(numbers)+1):
        numbers_square.append(numbers[j-1]**2)

    print((sum(numbers))**2 - sum(numbers_square))
main()
