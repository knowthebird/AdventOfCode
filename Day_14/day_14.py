#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 14, 2022.
"""
from os import path

def read_file(file_path):
    """ Return contents of the specified file.
    """
    with open(file_path, encoding='UTF-8') as file:
        return file.read().splitlines(False)

def get_points(inputs):
    """ Populate sets with all the points for each given range/path in the input.
    """
    points = []
    max_row = 0
    for line in inputs:
        split_pairs = line.split(' ')[0::2]
        vertices = []
        for pair in split_pairs:
            col = int(pair.split(',')[0])
            row = int(pair.split(',')[1])
            if row > max_row:
                max_row = row
            vertices.append([col,row])
        new_points = []
        for idx in range(len(vertices)-1):
            columns_in = [vertices[idx][0], vertices[idx+1][0]]
            rows_in = [vertices[idx][1], vertices[idx+1][1]]
            if columns_in[0] == columns_in[1]:
                new_points = [(columns_in[0], x) for x in range(min(rows_in), max(rows_in)+1)]
            elif rows_in[0] == rows_in[1]:
                new_points = [(x,rows_in[0]) for x in range(min(columns_in), max(columns_in)+1)]
            else:
                print("Unsupported Case!")
            points.extend(new_points)
    unique_points = set(points)
    return unique_points, max_row


def part_one(inputs):
    """ Placeholder function to return result to first part of puzzle.
    """
    points, max_row = get_points(inputs)
    sand_entry_point = (500,0)
    current_position = sand_entry_point
    sand = set()

    while current_position[1] < max_row:
        next_pos = next_position_to_fall(points, sand, current_position)
        if next_pos is not None:
            current_position = next_pos
        else:
            sand.add(current_position)
            current_position = (500,0)

    return len(sand)

def next_position_to_fall(points, sand, current_position):
    """ Return th next possible position if one exists, None otherwise.
    """
    # Down
    next_position = (current_position[0],current_position[1]+1)
    if (next_position not in points) and (next_position not in sand):
        return next_position

    # Left
    next_position = (current_position[0]-1,current_position[1]+1)
    if (next_position not in points) and (next_position not in sand):
        return next_position

    # Right
    next_position = (current_position[0]+1,current_position[1]+1)
    if (next_position not in points) and (next_position not in sand):
        return next_position

    return None


def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    points, max_row = get_points(inputs)
    max_row += 2
    sand_entry_point = (500,0)
    current_position = sand_entry_point
    sand = set()

    next_pos = next_position_to_fall(points, sand, current_position)
    while (current_position != sand_entry_point) or (next_pos is not None):
        if next_pos is not None:
            if next_pos[1] == max_row-1:
                sand.add(next_pos)
                current_position = (500,0)
            else:
                current_position = next_pos
        else:
            sand.add(current_position)
            current_position = (500,0)
        next_pos = next_position_to_fall(points, sand, current_position)

    return len(sand) +1

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
