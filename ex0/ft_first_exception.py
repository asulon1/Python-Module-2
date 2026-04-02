# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 17:51:59 by asulon          #+#    #+#               #
#  Updated: 2026/04/02 16:05:13 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def input_temperature(temp_str: str) -> int:
    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError(
            f"Caught input_temperature error: '{temp_str}' is not a valid number\n")
    if temperature > 40:
        raise ValueError(
            f"Caught input_temperature error: {temp_str}°C is too hot for plants (max 40°C)\n")
    if temperature < 0:
        raise ValueError(
            f"Caught input_temperature error: {temp_str}°C is too cold for plants (min 0°C)\n")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    inputs = ["25", "abc", "100", "-50"]

    for temp_str in inputs:
        print(f"Input data is '{temp_str}'")
        try:
            temperature = input_temperature(temp_str)
            temperature = int(temperature)
            print(f"Temperature is now {temperature}°C\n")
        except ValueError as error:
            print(f"{error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
