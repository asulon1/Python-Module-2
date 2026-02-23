# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 22:21:10 by asulon          #+#    #+#               #
#  Updated: 2026/02/23 22:48:15 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, plant_name: str, water_level: int, sun: int):
        if plant_name.strip() == "":
            raise ValueError("Plant name cannot be empty!\n")
        self.plant_name = plant_name
        self.water_level = water_level
        self.sun = sun


class GardenManager:
    garden = []

    def __init__(self, water_level: int):
        self.water_level = water_level

    def add_plant():
        pass

    def water_plants(water: int):
        if water < 1:
            raise ValueError(
                f"Water level {water} is too low (min 1)\n")
        if water > 10:
            raise ValueError(
                f"Water level {water} is too high (max 10)\n")
        for plant in GardenManager.garden:
            plant: Plant
            try:
                plant.water_level += water
            except ValueError as error:
                print()
            finally:
                print("Closing watering system (cleanup)")
            print(f"Watering {plant.plant_name} == success")

    def check_plant_health(self):
        if not isinstance(self.plant_name, str):
            raise ValueError("Plant name cannot be empty!\n")

        if self.water_level < 1:
            raise ValueError(
                f"Water level {self.water_level} is too low (min 1)\n")
        if self.water_level > 10:
            raise ValueError(
                f"Water level {self.water_level} is too high (max 10)\n")

        if self.sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {self.sunlight_hours} is too low (min 2)\n")
        if self.sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {self.sunlight_hours} is too high (max 12)\n")

        return f"{self.plant_name}': healthy(water)\n"

    pass


def test_garden_management():
    pass


if __name__ == "__main__":
    test_garden_management()
