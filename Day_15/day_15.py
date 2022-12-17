#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 15, 2022.
"""
from os import path

def read_file(file_path):
    """ Return contents of the specified file.
    """
    with open(file_path, encoding='UTF-8') as file:
        return file.read().splitlines(False)

def part_one(inputs, row_of_interest):
    """ Placeholder function to return result to first part of puzzle.
    """
    sensors, beacons, distances = load_inputs(inputs)

    possible_ranges = get_rows_valid_ranges(row_of_interest, sensors, distances)

    row_position_unavailable_for_new_beacon_count = 0
    for each_range in possible_ranges:
        row_position_unavailable_for_new_beacon_count += each_range[1]-each_range[0]-1

    beacons_already_in_row = 0
    for beacon in set(beacons):
        if beacon[1] == row_of_interest:
            beacons_already_in_row += 1

    non_beacon_positions = row_position_unavailable_for_new_beacon_count - beacons_already_in_row

    return non_beacon_positions

def load_inputs(inputs):
    """ Return sensors, beacons, and distances between them from the given inputs.
    """
    sensors = []
    beacons = []
    distances = []
    for line in inputs:
        split_line = line.split(' ')
        s_x = int(split_line[2][2:-1])
        s_y = int(split_line[3][2:-1])
        sensors.append((s_x,s_y))

        b_x = int(split_line[8][2:-1])
        b_y = int(split_line[9][2:])
        beacons.append((b_x,b_y))

        distances.append(get_distance((s_x,s_y), (b_x,b_y)))
    return sensors, beacons, distances

def get_distance(point_1, point_2):
    """ Return the taxicab / Manhattan distance between two points
    """
    return abs(point_1[0]-point_2[0])+abs(point_1[1]-point_2[1])

def get_rows_valid_ranges(current_row, sensors, distances):
    """ Determine what the possible ranges are where a value could be a beacon for the given row.
    For any given sensor and range, we can eleminate 0.5*range^2 possible positions.
    When we do this for all the sensors we greatly reduce the number of positions we need to check.
    Format is [[stop_x_index, start_x_index], [stop_x_index, start_x_index]]
    where any values inbetween stop and start indexes are not valid ranges to check.
    Stop and start indexes are still checked.
    """
    valid_ranges = []
    for idx, sensor in enumerate(sensors):
        y_diff = abs(current_row - sensor[1])
        if y_diff <= distances[idx]:
            stop_col = sensor[0]-abs(distances[idx]-y_diff)-1
            start_col = sensor[0]+abs(distances[idx]-y_diff)+1
            valid_ranges.append([stop_col,start_col])
    valid_ranges.sort(key=lambda x: x[0])
    return remove_overlap(valid_ranges)

def remove_overlap(values):
    """ Take the possible ranges provided, and remove any overlap in them.
    """
    new_values = [values[0]]
    for value in values:
        if value[0] < new_values[-1][1]:
            if value[1] > new_values[-1][1]:
                new_values[-1][1] = value[1]
        else:
            new_values.append(value)
    return new_values

def part_two(inputs, x_min, y_min, x_max, y_max):
    """ Placeholder function to return result to second part of puzzle.
    """
    sensors, _, distances = load_inputs(inputs)

    for row_idx in range(y_min,y_max+1):
        final_ranges = get_rows_valid_ranges(row_idx, sensors, distances)

        start = x_min
        stop = x_max
        for k, final_range in enumerate(final_ranges):
            if final_range[0] < start:
                start = final_range[1]
                if len(final_ranges) > k+1:
                    stop = min(final_ranges[k+1][0], x_max)
            elif final_range[0] == start:
                start = final_range[1]
                stop = min(final_range[1], x_max)
            elif final_range[0] > start:
                stop = final_range[0]

            # In our case, there will only be one location that can hold a
            # beacon, so we can return the first open space for one we find.
            if start <= stop+1:
                return ((start, row_idx)[0]*4000000)+(start, row_idx)[1]

    return None

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    print("Part One Sample: " + str(part_one(inputs, 10)))
    print("Part Two Sample: " + str(part_two(inputs, 0, 0, 20, 20)))
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs, 2000000)))
    print("Part Two: " + str(part_two(inputs, 0, 0, 4000000, 4000000)))

if __name__ == '__main__':
    main()
