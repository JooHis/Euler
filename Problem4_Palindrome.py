def check_palindrome(x):
    left_to_right = str(x)
    right_to_left = str(x)[::-1]
    if left_to_right == right_to_left:
        return True
    else:
        return False


def main():
    palindromes = []
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            x = int(i*j)
            if check_palindrome(x):
                palindromes.append((x, i, j))
                break
            else:
                continue
    palindromes.sort(reverse=True)
    for k in range(len(palindromes)-1, 0, -1):
        palindromes.pop(k)
    print(palindromes)


main()