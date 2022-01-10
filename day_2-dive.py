data_file = "files/day-1.txt"

coordinate = {"x": 0, "y": 0}

action = {
    "forward": ("x", 1),
    "down": ("y", 1),
    "up": ("y", -1),
}


def clean_and_cast(row: str) -> list:
    direction, number = row.strip("\n").split(" ")
    return direction, int(number)


with open("files/day-2.txt") as data:
    for row in data:
        direction, number = clean_and_cast(row)
        coord, multiply_by = action[direction]
        coordinate[coord] += multiply_by * number


print(coordinate.get("x") * coordinate.get("y"))
