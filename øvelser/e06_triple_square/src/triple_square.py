#!/usr/bin/env python3


def triple(number):
    return number * 3


def square(number):
    return number ** 2


def main():
    for number in range(1, 11):
        tr = triple(number)
        sq = square(number)

        if (sq > tr):
            break
        print(f"triple({number})=={tr} square({number})=={sq}")


if __name__ == "__main__":
    main()
