#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 20, 2022.
"""
from os import path

def read_file(file_path):
    """ Return contents of the specified file.
    """
    with open(file_path, encoding='UTF-8') as file:
        return file.read().splitlines(False)

def part_one(inputs):
    """ Placeholder function to return result to first part of puzzle.
    """
    inputs = [int(x) for x in inputs]
    mixed_idxs = list(range(len(inputs)))

    for input_idx, position_change in enumerate(inputs):
        start_position = mixed_idxs.index(input_idx)
        mixed_idxs.pop(start_position)
        new_position = (start_position + position_change) % len(mixed_idxs)
        mixed_idxs.insert(new_position, input_idx)

    grove_coordinates = []
    start_pos = mixed_idxs.index(inputs.index(0))
    grove_coordinates.append(inputs[mixed_idxs[(start_pos + 1000) % len(mixed_idxs)]])
    grove_coordinates.append(inputs[mixed_idxs[(start_pos + 2000) % len(mixed_idxs)]])
    grove_coordinates.append(inputs[mixed_idxs[(start_pos + 3000) % len(mixed_idxs)]])

    return sum(grove_coordinates)

def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    decryption_key = 811589153
    inputs = [(int(x) * decryption_key) for x in inputs]
    mixed_idxs = list(range(len(inputs)))
    for _ in range(10):
        for input_idx, position_change in enumerate(inputs):
            start_position = mixed_idxs.index(input_idx)
            mixed_idxs.pop(start_position)
            new_position = (start_position + position_change) % len(mixed_idxs)
            mixed_idxs.insert(new_position, input_idx)

    grove_coordinates = []
    start_pos = mixed_idxs.index(inputs.index(0))
    grove_coordinates.append(inputs[mixed_idxs[(start_pos + 1000) % len(mixed_idxs)]])
    grove_coordinates.append(inputs[mixed_idxs[(start_pos + 2000) % len(mixed_idxs)]])
    grove_coordinates.append(inputs[mixed_idxs[(start_pos + 3000) % len(mixed_idxs)]])

    return sum(grove_coordinates)

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    print("Sampe Part One: " + str(part_one(inputs)))
    print("Sample Part Two: " + str(part_two(inputs)))
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
