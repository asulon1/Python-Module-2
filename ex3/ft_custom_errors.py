# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 19:26:47 by asulon          #+#    #+#               #
#  Updated: 2026/04/02 16:05:56 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred!") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def check_plant_health(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError()


def check_water_tank(current_liters: float, minimum_required: float) -> None:
    if current_liters < minimum_required:
        raise WaterError()


def test_specific_errors() -> None:
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


def test_catch_all_garden_errors() -> None:
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


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_specific_errors()
    test_catch_all_garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
