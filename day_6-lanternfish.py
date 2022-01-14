from collections import Counter

file_path = "files/day-6.txt"

with open(file_path) as data:
    fish_list = [int(fish_state) for fish_state in next(data).split(",")]


# Part One - Naive Approach
def simulate_fish_population(fish_list: list, days: int) -> int:
    fish_list = fish_list.copy()
    fishes_to_create = 0

    for _ in range(days):
        for index, fish in enumerate(fish_list):
            if fish == 0:
                fish_list[index] = 6
                fishes_to_create += 1
            else:
                fish_list[index] -= 1

        for new_fish in range(fishes_to_create):
            fish_list.append(8)

        fishes_to_create = 0

    return len(fish_list)


print(simulate_fish_population(fish_list, 80))


# Part Two - more optimal solution
def simulate_fish_population_two(fish_list: list, days: int) -> int:
    fish_counter = Counter(fish_list)

    for _ in range(days):
        # copy must be used, so that dictionary does not change its size during iteration
        cnt_copy = fish_counter.copy()

        for state, amount in fish_counter.items():
            if state == 0:
                cnt_copy[0] -= amount
                cnt_copy[6] += amount
                cnt_copy[8] += amount

            elif amount > 0:
                cnt_copy[state] -= amount
                cnt_copy[state - 1] += amount

            fish_counter = cnt_copy

    return sum(value for value in fish_counter.values())


print(simulate_fish_population_two(fish_list, 256))