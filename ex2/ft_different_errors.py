# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 18:37:42 by asulon          #+#    #+#               #
#  Updated: 2026/04/02 17:35:31 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            try:
                int('abc')
            except ValueError as error:
                raise ValueError(f"Caught ValueError: {error}\n")
        case 1:
            try:
                100 / 0
            except ZeroDivisionError as error:
                raise ZeroDivisionError(f"Caught ZeroDivisionError: {error}\n")
        case 2:
            try:
                f = open("missing.txt")
                f.close()
            except FileNotFoundError as error:
                raise FileNotFoundError(f"Caught FileNotFoundError: {error}\n")
        case 3:
            try:
                i = "abc"
                i += 1
            except TypeError as error:
                raise TypeError(f"Caught KeyError: {error}\n")
        case _:
            print("Operation completed successfully\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for x in [0, 1, 2, 3, 4]:
        try:
            print(f"Testing operation {x}...")
            garden_operations(x)

        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as error:
            print(error)

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
