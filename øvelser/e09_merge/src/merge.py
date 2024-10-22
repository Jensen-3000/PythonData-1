#!/usr/bin/env python3

def merge(L1, L2):
    i, j = 0, 0
    lst = []

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            lst.append(L1[i])
            i += 1
        else:
            lst.append(L2[j])
            j += 1

    lst.extend(L1[i:])
    lst.extend(L2[j:])

    return lst


def main():

    L1 = [1, 5, 9, 12]
    L2 = [2, 6, 10]

    lst = merge(L1, L2)
    print(lst)


if __name__ == "__main__":
    main()
