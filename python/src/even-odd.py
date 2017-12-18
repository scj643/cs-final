#!/usr/bin/env python3
def even_odd():
    i = 0
    evens = 0
    odds = 0
    while i != -1:
        i = int(input("Please enter a positive number. Enter -1 to stop"))
        if i < -1:
            print("Must be positive")
        elif i > 0:
            if i % 2:
                odds += 1
            else:
                evens += 1
        if odds > evens:
            print("More odds entered than evens.")
        if evens > odds:
            print("More evens entered than odds.")
        if odds == evens:
            print("Equal amount of even and odds entered.")

if __name__ == '__main__':
    even_odd()