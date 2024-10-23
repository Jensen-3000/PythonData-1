#!/usr/bin/env python3

def transform(s1, s2):

    l1 = s1.split()
    l2 = s2.split()

    z = zip(map(int, l1), map(int, l2))

    return [i*j for i, j in z]


def main():

    print(transform("1 5 3", "2 6 -1"))

    pass


if __name__ == "__main__":
    main()
