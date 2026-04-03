# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 19:48:12 by asulon          #+#    #+#               #
#  Updated: 2026/04/03 16:45:53 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred!") -> None:
        super().__init__("Caught " + message)


class PlantError(GardenError):
    def __init__(self, message: str = "Plant is wilting!") -> None:
        super().__init__(f"PlantError: {message}")


def water_plant(plant_name: str) -> None:
    try:
        if plant_name[0].isupper():
            print(f"Watering {plant_name}: [OK]")
        else:
            raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    except ValueError as error:
        raise PlantError(f"{error}")


def test_watering_system():
    valid_list = ["Tomato", "Lettuce", "Carrots"]
    invalid_list = ["Tomato", "lettuce"]
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in valid_list:
            water_plant(plant)
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant in invalid_list:
            water_plant(plant)
    except PlantError as error:
        print(error)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
