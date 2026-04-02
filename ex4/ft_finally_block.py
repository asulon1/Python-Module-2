# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 19:48:12 by asulon          #+#    #+#               #
#  Updated: 2026/02/23 20:11:46 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def water_plants(plant_list: list):
    print("Testing normal watering...")
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str) or plant.strip() == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")


def test_watering_system():
    correct_list = ["tomato", "lettuce", "carrots"]
    error_list = ["tomato", None, "ototot"]
    print("=== Garden Watering System ===\n")

    water_plants(correct_list)
    water_plants(error_list)
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_watering_system()
