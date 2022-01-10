data_file = "files/day-1.txt"

coordinate = {"x": 0, "y": 0, "aim": 0}

action = {
    "forward": ("x", 1),
    "down": ("aim", 1),
    "up": ("aim", -1),
}


def clean_and_cast(row: str) -> list:
    direction, number = row.strip("\n").split(" ")
    return direction, int(number)


with open("files/day-2.txt") as data:
    for row in data:
        direction, number = clean_and_cast(row)
        coord, multiply_by = action[direction]
        coordinate[coord] += multiply_by * number

        if direction == "forward":
            coordinate["y"] += coordinate["aim"] * number

print(coordinate.get("x") * coordinate.get("y"))
