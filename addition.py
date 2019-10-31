#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This adds user numbers except negatives


def main():
    # this adds user numbers except negatives
    # helps revents crashing
    while True:
        # prgrams main function
        try:
            # list of all positive numbers
            total_numbers = []

            # input
            number = int(input("How many numbers are you going to add: "))
            print()

            # process
            for addition in range(number):
                numbers = int(input("Enter a number to add: "))

                if numbers < 0:
                    continue

                total_numbers.append(numbers)

            # output
            print()
            print("Sum of just the positive numbers is =", sum(total_numbers))

        # prevents false user inputs
        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        # break out of loop
        else:
            break


if __name__ == "__main__":
    main()
