# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 17:51:59 by asulon          #+#    #+#               #
#  Updated: 2026/04/02 17:12:45 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def input_temperature(temp_str: str) -> int:
    try:
        temperature = int(temp_str)
    except ValueError as error:
        raise ValueError(f"{error}\n")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    inputs = ["25", "abc"]

    for temp_str in inputs:
        print(f"Input data is '{temp_str}'")
        try:
            temperature = input_temperature(temp_str)
            temperature = int(temperature)
            print(f"Temperature is now {temperature}°C\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
