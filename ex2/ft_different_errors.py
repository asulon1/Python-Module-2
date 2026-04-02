# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 18:37:42 by asulon          #+#    #+#               #
#  Updated: 2026/04/02 17:25:33 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            try:
                int('abc')
            except ValueError as error:
                print(f"Caught ValueError: {error}\n")
        case 1:
            try:
                100 / 0
            except ZeroDivisionError as error:
                print(f"Caught ZeroDivisionError: {error}\n")
        case 2:
            try:
                f = open("missing.txt")
                f.close()
            except FileNotFoundError as error:
                print(f"Caught FileNotFoundError: {error}\n")
        case 3:
            try:
                plant_data: dict[str, int] = {"rose": 1, "sunflowe": 2}
                plant_data['missing_plant']
            except KeyError as error:
                print(f"Caught KeyError: {error}\n")
        case _:
            print("Operation completed successfully\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for x in [0, 1, 2, 3, 4]:
        try:
            print(f"Testing operation {x}...")
            garden_operations(x)

        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
