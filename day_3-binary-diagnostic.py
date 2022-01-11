from functools import partial

data_file = "files/day-3.txt"

to_decimal_number = partial(int, base=2)


def initialize_counter(max_index: int) -> dict:
    return dict.fromkeys(range(max_index), 0)


def clean_row(row: str) -> str:
    return row.strip("\n")


def update_counter(counter: dict, binary_number: str) -> None:
    for index, digit in enumerate(binary_number):
        if binary_number[index] == "1":
            counter[index] += 1


def get_gamma_rate(counter: dict, rows_count: int) -> int:
    digits = []

    for index in range(digits_count):
        count_for_one = counter.get(index)
        digit = 0 if count_for_one < rows_count / 2 else 1
        digits.append(digit)

    binary_string = "".join(str(num) for num in digits)
    print(binary_string)
    return to_decimal_number(binary_string)


with open(data_file) as data:
    # PART ONE
    rows_count = 0
    row = clean_row(next(data))
    digits_count = len(row)

    # initializing counter for count of 1 in binary number for each index
    counter = initialize_counter(digits_count)

    # resetting cursor to its initial position
    data.seek(0)

    for row in data:
        row = clean_row(row)
        update_counter(counter, row)
        rows_count += 1

    max_number = 2 ** digits_count - 1
    gamma_rate = get_gamma_rate(counter, rows_count)
    epsilon_rate = max_number - gamma_rate
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)
