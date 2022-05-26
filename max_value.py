#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 25, 2022
# This program generates 10 random numbers between 1 and 100 and
# displays them to the user and then finds the max value of the numbers

import random


def get_max_value(array_of_num):
    # declare variable
    max_value = -1

    # find the max value
    for counter in range(0, len(array_of_num)):
        if array_of_num[counter] > max_value:
            max_value = array_of_num[counter]

    return max_value


def main():
    # declare constants
    MAX_SIZE = 10
    MAX_NUM = 100
    MIN_NUM = 1

    # create an empty list
    array_of_num = []

    for counter in range(0, MAX_SIZE):
        # generate random number
        random_number = random.randint(MIN_NUM, MAX_NUM)

        # add the number to the list
        array_of_num.append(random_number)

        max_value = get_max_value(array_of_num)
        # print the random number generated and the position it is in the list
        print(
            "{} added to the list at position {}".format(array_of_num[counter], counter)
        )

    print()
    print("The max value is: {}".format(max_value))


if __name__ == "__main__":
    main()
