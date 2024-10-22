#!/usr/bin/env python3

def reverse_dictionary(d):

    rd = {}

    for key, value in d.items():
        for i in value:
            if i in rd:
                rd[i].append(key)
            else:
                rd[i] = [key]

    return rd


def main():

    d = {'move': ['liikuttaa'], 'hide': ['piilottaa',
                                         'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
