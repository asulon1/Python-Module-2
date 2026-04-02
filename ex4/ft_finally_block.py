# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 19:48:12 by asulon          #+#    #+#               #
#  Updated: 2026/04/02 18:27:29 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred!") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str = "Unknown", message: str = "Plant is wilting!") -> None:
        super().__init__(name + ' ' + message)


def water_plant(plant_name: str) -> None:
    try:
        if not plant_name.capitalize():
            raise ValueError(f"Cannot water {plant} - invalid plant!")
        print(f"Watering {plant}: [OK]")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")


def test_watering_system():
    print("Testing valid plants...")
    print("Opening watering system")
    print("")
    print("=== Garden Watering System ===\n")

    water_plant()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_watering_system()
