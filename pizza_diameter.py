#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Feb 2022
# This program calculates the price of a pizza
#    with diameter inputted by the user and HST

import constants


def main():
    # this function calculates the circumference

    # input
    diameter = float(input("Enter the diameter of the pizza (inch): "))

    # process
    pizza_price = (
        constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    )
    total = pizza_price + (pizza_price * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
