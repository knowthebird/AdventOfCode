#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 9, 2022.
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
    head_row, head_column, tail_row, tail_column = 0,0,0,0
    visited = []

    for line in inputs:
        match line[0]:
            case "U":
                add = [1,0]
            case "D":
                add = [-1,0]
            case "L":
                add = [0,-1]
            case "R":
                add = [0,1]

        spaces_to_move = int(line[1:])
        for _ in range(spaces_to_move):
            head_row += add[0]
            head_column += add[1]
            tail_row, tail_column = move_tail(head_row, head_column, tail_row, tail_column)
            visited.append((tail_row, tail_column))

    return len(set(visited))

def move_tail(head_row, head_column, tail_row, tail_column):
    """ Updates the positions of the tail after the head is moved according to
    the puzzle rules. """
    if (head_row > tail_row + 1) and (head_column > tail_column):
        tail_row += 1
        tail_column += 1
    elif (head_row > tail_row + 1) and (head_column < tail_column):
        tail_row += 1
        tail_column -= 1
    elif head_row > tail_row + 1:
        tail_row += 1
    elif (head_row < tail_row - 1) and (head_column > tail_column):
        tail_row -= 1
        tail_column += 1
    elif (head_row < tail_row - 1) and (head_column < tail_column):
        tail_row -= 1
        tail_column -= 1
    elif head_row < tail_row - 1:
        tail_row -= 1
    elif (head_column > tail_column + 1) and (head_row > tail_row):
        tail_row += 1
        tail_column += 1
    elif (head_column > tail_column + 1) and (head_row < tail_row):
        tail_row -= 1
        tail_column += 1
    elif head_column > tail_column + 1:
        tail_column += 1
    elif (head_column < tail_column - 1) and (head_row > tail_row):
        tail_row += 1
        tail_column -= 1
    elif (head_column < tail_column - 1) and (head_row < tail_row):
        tail_row -= 1
        tail_column -= 1
    elif head_column < tail_column - 1:
        tail_column -= 1

    return tail_row, tail_column

def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    total_knots = 10
    knot_positions = []
    for _ in range(total_knots):
        knot_positions.append([0,0])
    visited = []

    for line in inputs:
        match line[0]:
            case "U":
                add = [1,0]
            case "D":
                add = [-1,0]
            case "L":
                add = [0,-1]
            case "R":
                add = [0,1]

        spaces_to_move = int(line[1:])
        for _ in range(spaces_to_move):
            knot_positions[0] = [sum(x) for x in zip(knot_positions[0], add)]
            visited.append(track_tail(knot_positions))

    return len(set(visited))

def track_tail(knot_positions):
    """ Updates the positions of each knot in the rope after the head is moved
    according to the puzzle rules, then returns the position of the tail. """
    for i in range(len(knot_positions)-1):
        knot_positions[i+1][0], knot_positions[i+1][1] = \
        move_tail(knot_positions[i][0], knot_positions[i][1], \
        knot_positions[i+1][0], knot_positions[i+1][1])
    return (knot_positions[9][0], knot_positions[9][1])

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
