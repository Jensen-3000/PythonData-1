#!/usr/bin/env python3

import math


def triangle_area(h, b):
    return 0.5 * h * b


def rectangle_area(a, b):
    return a * b


def circle_area(r):
    return math.pi * r**2


def printShape(area):
    print(f"The area is {area:f}")


def inputPromt(size, shape):
    userInput = input("Give {size} of the {shape}: ")
    return float(userInput)


def main():
    # enter you solution here

    while (True):

        shapeInput = input("Choose a shape (triangle, rectangle, circle): ")
        if shapeInput == "":
            break

        if shapeInput == "triangle":
            base = inputPromt("base", shapeInput)
            height = inputPromt("height", shapeInput)
            area = triangle_area(base, height)

        elif shapeInput == "rectangle":
            width = inputPromt("width", shapeInput)
            height = inputPromt("height", shapeInput)
            area = rectangle_area(width, height)

        elif shapeInput == "circle":
            radius = inputPromt("radius", shapeInput)
            area = circle_area(radius)

        else:
            print("Unknown shape!")
            continue

        printShape(area)


if __name__ == "__main__":
    main()
