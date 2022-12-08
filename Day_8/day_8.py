#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 8, 2022.
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
    total_columns = len(inputs[0])
    total_rows = len(inputs)
    total_trees_visible = 2 * total_columns + 2 * (total_rows -2)

    for column in range(1,total_columns-1):
        for row in range(1,total_rows-1):
            if is_visible(inputs, row, column):
                total_trees_visible += 1

    return total_trees_visible

def is_visible(inputs, row, column):
    """ Returns if the tree is visible from outside the forest.
    """
    height = inputs[row][column]

    # View from the top
    if all(inputs[check_row][column] < height for check_row in range(row)):
        return True

    # View from the bottom
    if all(inputs[check_row][column] < height for check_row in range(row+1, len(inputs))):
        return True

    # View from the left
    if all(inputs[row][check_column] < height for check_column in range(column)):
        return True

    # View from the right
    if all(inputs[row][check_column] < height for check_column in range(column+1,len(inputs[0]))):
        return True

    return False

def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    total_columns = len(inputs[0])
    total_rows = len(inputs)

    max_score = 0
    for column in range(total_columns):
        for row in range(total_rows):
            current_score = scenic_score(inputs, row, column)
            if current_score > max_score:
                max_score = current_score
    return max_score

def scenic_score(inputs, row, column):
    """ Calculate the scenic score for a given tree in the forest.
    """
    height = inputs[row][column]

    top = 0
    for check_row in reversed(range(row)):
        top += 1
        if inputs[check_row][column] >= height:
            break

    bottom = 0
    for check_row in range(row+1, len(inputs)):
        bottom += 1
        if inputs[check_row][column] >= height:
            break

    left = 0
    for check_column in reversed(range(column)):
        left += 1
        if inputs[row][check_column] >= height:
            break

    right = 0
    for check_column in range(column+1,len(inputs[0])):
        right += 1
        if inputs[row][check_column] >= height:
            break

    return top * bottom * left * right

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
