from functools import partial
from collections import deque

data_file = "files/day-3.txt"

# binary number string → int of base 10
to_decimal_number = partial(int, base=2)


def initialize_keys_from_range(max_index: int) -> dict:
    return dict.fromkeys(range(max_index), 0)


# returns false if 0 is set and true if 1 is set for a given position at binary number string
def is_nth_bit_set(bin_number: str, index: int) -> bool:
    number = to_decimal_number(bin_number)
    return bool((2 ** index) & number)


def update_counter(counter: dict, bin_number: str, max_index: int) -> None:
    for index in range(max_index):
        # given_position += 1 or 0
        counter[index] += is_nth_bit_set(bin_number, index)


def get_gamma_rate(counter: dict, count: int, max_index: int) -> int:
    final_bin_digits = deque()

    for index in range(max_index):
        digit = counter.get(index)
        half_count_of_iterations = count / 2
        digit = 1 if digit > half_count_of_iterations else 0
        final_bin_digits.appendleft(digit)

    binary_string = "".join(str(num) for num in final_bin_digits)
    return to_decimal_number(binary_string)


with open(data_file) as data:
    first_number = next(data).strip("\n")

    # max value which can be represented by binary number in the file
    # e.g.: 1111 → 15, 11111111 → 255
    max_num = 2 ** len(first_number) - 1
    max_index = len(first_number)
    counter = initialize_keys_from_range(max_index)
    iterations_count = 0

    # returning cursor back to its initial position
    data.seek(0)

    for number in data:
        number = number.strip("\n")
        update_counter(counter, number, max_index)
        iterations_count += 1


gamma_rate = get_gamma_rate(counter, iterations_count, max_index)
epsilon_rate = max_num - gamma_rate
power_consumption = epsilon_rate * gamma_rate
print(power_consumption)