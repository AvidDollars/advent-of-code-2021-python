data_file = "files/day-1.txt"

with open(data_file) as data:

    prev_measurement = next(data)
    increased_count = 0

    for measurement in data:
        if int(measurement) > int(prev_measurement):
            increased_count += 1
        prev_measurement = measurement

print(increased_count)