from math import ceil, floor


def main():
    for i in range(997, 3, -1):
        c = int(i)
        ref_point = (1000-c)/2
        if ref_point % 1 != 0:
            a = floor(ref_point)
            b = ceil(ref_point)
        else:
            a = ref_point-1
            b = ref_point+1
        while a >= 1 and b <= c-1:
            if a**2 + b**2 == c**2:
                return print(a, b, c)
            a -= 1
            b += 1


main()



main()