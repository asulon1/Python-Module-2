# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 17:51:59 by asulon          #+#    #+#               #
#  Updated: 2026/02/23 19:14:28 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str):
    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number\n")
    if temperature > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)\n")
    if temperature < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)\n")
    return temperature


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    inputs = ["25", "abc", "100", "-50"]

    for temp_str in inputs:
        print(f"Testing temperature: {temp_str}")
        try:
            temperature = check_temperature(temp_str)
            if temperature.is_integer():
                temperature = int(temperature)
            print(f"Temperature {temperature}°C is perfect for plants!\n")
        except ValueError as error:
            print(f"Error: {error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
