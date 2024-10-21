#!/usr/bin/env python3

def main():

    diceOne = range(1, 7)
    diceTwo = range(1, 7)

    for i in diceOne:
        for j in diceTwo:
            if i + j == 5:
                print((i, j))

    pass


if __name__ == "__main__":
    main()
