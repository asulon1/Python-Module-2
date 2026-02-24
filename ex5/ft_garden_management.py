# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 22:21:10 by asulon          #+#    #+#               #
#  Updated: 2026/02/24 17:50:45 by asulon          ###   ########.fr        #
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


class Plant:
    def __init__(self, plant_name: str, water_level: int, sun: int):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sun = sun

    # Watering plant
    def water_plant(self):
        print(f"Watering {self.plant_name} - success")


class GardenManager:
    def __init__(self):
        self.plants: list[Plant] = []

    # Add plant in garden
    def add_plants(self, plant_list: list[Plant]):
        for plant in plant_list:
            if plant.plant_name.strip() == "":
                raise ValueError(
                    "Plant name cannot be empty!\n")
            self.plants.append(plant)
            print(f"Added {plant.plant_name} successfully")

    # Make each plants bigger
    def water_plants(self):
        print("Opening watering system")
        for plant in self.plants:
            plant.water_plant()

    # Check health of plants in the garden
    def check_plant_health(self):
        for plant in self.plants:
            if (not isinstance(plant.plant_name, str) or
                    plant.plant_name.strip() == ""):
                raise ValueError("Plant name cannot be empty!\n")

            if plant.water_level < 1:
                raise ValueError(
                    f"Water level {plant.water_level} is too low (min 1)\n")
            if plant.water_level > 10:
                raise ValueError(
                    f"Water level {plant.water_level} is too high (max 10)\n")

            if plant.sun < 2:
                raise ValueError(
                    f"Sunlight hours {plant.sun} is too low (min 2)\n")
            if plant.sun > 12:
                raise ValueError(
                    f"Sunlight hours {plant.sun} is too high (max 12)\n")

            print(
                f"{plant.plant_name}: healthy "
                f"(water: {plant.water_level}, sun: {plant.sun})")


def test_garden_management():
    # Add plants
    try:
        print("Adding plants to garden...")
        manager = GardenManager()
        plant_list = [
            Plant("tomato", 5, 8),
            Plant("lettuce", 15, 5),
            Plant("   ", 4, 5),
        ]

        manager.add_plants(plant_list)
    except ValueError as error:
        print(f"Error adding plant: {error}")

    # Water plants
    try:
        print("Watering plants...")
        manager.water_plants()
    except ValueError as error:
        print(f"Error adding plant: {error}")
    finally:
        print("Closing watering system (cleanup)\n")

    # Check health
    try:
        print("Checking plant health...")
        manager.check_plant_health()
    except ValueError as error:
        print(f"Error checking lettuce: {error}")
    # Recovery

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
