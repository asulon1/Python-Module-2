# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 18:37:42 by asulon          #+#    #+#               #
#  Updated: 2026/02/23 19:25:59 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations():
    try:
        print("Testing ValueError...")
        int('abc')
    except ValueError as error:
        print(f"Caught ValueError: {error}\n")
    try:
        print("Testing ZeroDivisionError...")
        100 / 0
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}\n")
    try:
        print("Testing FileNotFoundError...")
        f = open("missing.txt")
        f.close()
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}\n")
    try:
        print("Testing KeyError...")
        plant_data = {}
        _ = plant_data['missing_plant']
    except KeyError as error:
        print(f"Caught KeyError: {error}\n")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    try:
        garden_operations()

    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
