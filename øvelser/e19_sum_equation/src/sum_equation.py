#!/usr/bin/env python3


def sum_equation(L):
    # if not L:
    #     return "0 = 0"

    # s = [str(i) for i in L]
    # s2 = f"{' + '.join(s)} = {sum(L)}"
    # return s2

    # OneLiner er street
    return f"{' + '.join([str(i) for i in L])} = {sum(L)}" if L else "0 = 0"


def main():
    print(sum_equation([1, 5, 7]))
    print(sum_equation([]))


if __name__ == "__main__":
    main()
