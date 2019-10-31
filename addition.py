#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This lets the user guess a number


def main():
    while True:
        try:
            total_numbers = []

            number = int(input("How many numbers are you going to add: "))
            print()

            for addition in range(number):
                numbers = int(input("Enter a number to add: "))

                if numbers < 0:
                    continue

                total_numbers.append(numbers)

            print()
            print("Sum of just the positive numbers is =", sum(total_numbers))

        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
