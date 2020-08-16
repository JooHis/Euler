from itertools import permutations

def main():
    s1 = "RR"
    s2 = "DD"

    # Get all permutations of length 2
    # and length 2
    perm = set(permutations(["R", "R", "D", "D", "R", "R", "D", "D", "R", "R", "D", "D", "R", "R", "D", "D", "R", "R", "D", "D", ], 7))

    # Print the obtained permutations
    for i in list(perm):
        print(i)
main()



'''RRDD, DDRR, RDRD, DRDR, RDDR, DRRD'''