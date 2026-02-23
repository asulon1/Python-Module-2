# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 19:26:47 by asulon          #+#    #+#               #
#  Updated: 2026/02/23 19:45:50 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message="A garden error occurred!"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def check_plant_health(is_wilting):
    if is_wilting:
        raise PlantError()


def check_water_tank(current_liters, minimum_required):
    if current_liters < minimum_required:
        raise WaterError()


def test_specific_errors():
    print("Testing PlantError...")
    try:
        check_plant_health(True)
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    print("Testing WaterError...")
    try:
        check_water_tank(2, 5)
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")


def test_catch_all_garden_errors():
    print("Testing catching all garden errors...")
    checks = [
        lambda: check_plant_health(True),
        lambda: check_water_tank(1, 3),
    ]

    for check in checks:
        try:
            check()
        except GardenError as error:
            print(f"Caught a garden error: {error}")


def main():
    print("=== Custom Garden Errors Demo ===")
    test_specific_errors()
    test_catch_all_garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
