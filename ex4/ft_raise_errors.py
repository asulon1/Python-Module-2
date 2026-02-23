# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 20:12:49 by asulon          #+#    #+#               #
#  Updated: 2026/02/23 22:20:23 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_plant_health(plant_name, water_level, sunlight_hours):
    if not isinstance(plant_name, str) or plant_name.strip() == "":
        raise ValueError("Plant name cannot be empty!\n")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")

    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)\n")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)\n")

    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    try:
        print("Testing good values...")
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")

    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 8)
    except ValueError as error:
        print(f"Error: {error}")

    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 8)
    except ValueError as error:
        print(f"Error: {error}")

    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as error:
        print(f"Error: {error}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
