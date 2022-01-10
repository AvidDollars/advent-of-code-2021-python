from collections import deque

data_file = "files/day-1.txt"

with open(data_file) as data:

    # PART ONE
    prev_measurement = next(data)
    increased_count = 0

    for measurement in data:
        if int(measurement) > int(prev_measurement):
            increased_count += 1
        prev_measurement = measurement

    # PART TWO
    data.seek(0) # cursor reset
    measurements = deque(maxlen=3)

    # initializing deque with first 3 measurements
    for _ in range(3):
        measurement = int(next(data))
        measurements.append(measurement)

    counter = 0

    for current in data:
        current = int(current)
        if (current + measurements[1] + measurements[2]) > sum(measurements):
            counter += 1
        measurements.append(current)

print(increased_count)
print(counter)