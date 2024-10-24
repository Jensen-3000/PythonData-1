#!/usr/bin/env python3

import math


class Rational(object):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.reduce()

    def reduce(self):
        gcd = math.gcd(self.n1, self.n2)
        self.n1 //= gcd
        self.n2 //= gcd

    def __str__(self):
        return f"{self.n1}/{self.n2}"

    def __mul__(self, other):
        return Rational(self.n1 * other.n1, self.n2 * other.n2)

    def __truediv__(self, other):
        return Rational(self.n1 * other.n2, self.n2 * other.n1)

    def __add__(self, other):
        return Rational(self.n1 * other.n2 + other.n1 * self.n2, self.n2 * other.n2)

    def __sub__(self, other):
        return Rational(self.n1 * other.n2 - other.n1 * self.n2, self.n2 * other.n2)

    def __eq__(self, other):
        return self.n1 * other.n2 == other.n1 * self.n2

    def __lt__(self, other):
        return self.n1 * other.n2 < other.n1 * self.n2

    def __gt__(self, other):
        return self.n1 * other.n2 > other.n1 * self.n2


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
