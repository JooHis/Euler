

def main():
    n = int(13)
    jonot = []
    while n < 1000000:
        k = n
        l = 1
        while k != 1:
            if str(k)[-1:] in "02468":
                k = int(k / 2)
            else:
                k = (3 * k) + 1
            l += 1
        jonot.append(l)
        n += 1

    maksimi = max(jonot)
    print(list.index(jonot, maksimi) + 13, maksimi)

main()