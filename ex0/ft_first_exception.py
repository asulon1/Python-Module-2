# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 17:51:59 by asulon          #+#    #+#               #
#  Updated: 2026/02/19 18:34:32 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str):
    try:
        print(f"Testing temperature: {temp_str}")
        if int(temp_str) > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
        elif int(temp_str) < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {temp_str}°C is good for plant!\n")
    except ValueError:
        print(f"Error : '{temp_str}' is not a valid number\n")


def main():
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
