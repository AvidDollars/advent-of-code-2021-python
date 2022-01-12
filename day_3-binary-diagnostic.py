from functools import partial
from operator import add, sub

data_file = "files/day-3.txt"

to_decimal_number = partial(int, base=2)


def initialize_counter(max_index: int) -> dict:
    return dict.fromkeys(range(max_index), 0)


def clean_row(row: str) -> str:
    return row.strip("\n")


def update_counter(counter: dict, binary_number: str, *, operation=add) -> None:
    for index, digit in enumerate(binary_number):
        if digit == "1":
            counter[index] = operation(counter[index], 1)


def get_gamma_rate(counter: dict, rows_count: int) -> int:
    digits = []

    for index in range(digits_count):
        count_for_one = counter.get(index)
        digit = 0 if count_for_one < rows_count / 2 else 1
        digits.append(digit)

    binary_string = "".join(str(num) for num in digits)
    return to_decimal_number(binary_string)


# PART ONE
with open(data_file) as data:
    rows_count = 0
    row = clean_row(next(data))
    digits_count = len(row)

    # list of string binary numbers → to be used for part two
    binary_numbers_list = []

    # initializing counter for count of 1 in binary number for each index
    counter = initialize_counter(digits_count)

    # resetting cursor to its initial position
    data.seek(0)

    for row in data:
        row = clean_row(row)
        update_counter(counter, row)
        binary_numbers_list.append(row)
        rows_count += 1

    max_number = 2 ** digits_count - 1
    gamma_rate = get_gamma_rate(counter, rows_count)
    epsilon_rate = max_number - gamma_rate
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)


# PART TWO
def get_chemical_rating(numbers_list: list, counter: dict, *, most_common_bit: int) -> int:

    # making a copy (in order to not to mutate original list and dict)
    numbers_list = list(numbers_list)
    counter = dict(counter)

    valid_numbers_count = len(numbers_list)
    current_index = 0

    while valid_numbers_count > 1:

        valid_bit = f"{0 ^ most_common_bit}" \
            if counter.get(current_index) >= (valid_numbers_count / 2) \
            else f"{1 ^ most_common_bit}"

        for number_index, number in enumerate(numbers_list):
            if (number is not None) and (number[current_index] != valid_bit):
                update_counter(counter, number, operation=sub)

                # setting invalid number to None
                numbers_list[number_index] = None
                valid_numbers_count -= 1

        current_index += 1

    # returning first number which is not None
    binary_string = next(num for num in numbers_list if num)
    return to_decimal_number(binary_string)


oxygen_generator = get_chemical_rating(binary_numbers_list, counter, most_common_bit=1)
carbon_dioxide_scrubber = get_chemical_rating(binary_numbers_list, counter, most_common_bit=0)
print(oxygen_generator * carbon_dioxide_scrubber)