#!/usr/bin/env python3
def breaths(age):
    """

    :param age: age in years
    :return:
    """
    total = 0
    while age != -1:
        if age == 0:
            total += 25 * 525600
        if age in range(1,4):
            total += 20 * 525600
        if age in range(5,14):
            total += 15 * 525600
        if age > 15:
            total += 11 * 525600
        age -= 1
    return total

if __name__ == "__main__":
    a = int(input("What's your age?"))
    print("you have taken about {} breaths.".format(breaths(a)))
    print("Your heart has beat about {} times".format(a*67.5*525600))