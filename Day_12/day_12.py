#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 12, 2022.
"""
from os import path
from string import ascii_lowercase

def read_file(file_path):
    """ Return contents of the specified file.
    """
    with open(file_path, encoding='UTF-8') as file:
        return file.read().splitlines(False)

def breadth_first_search(graph, current_node, desired_node):
    """ Slightly modified breath first search to return the shortest
    set of steps to reach the desired_node from the current_node.
    """
    queue = [current_node]
    moves = ["S"]
    visited = [current_node]

    while queue:
        head = queue.pop(0)
        moves_to_head = moves.pop(0)
        if head == desired_node:
            moves_to_head += "E"
            return moves_to_head, len(moves_to_head)-2

        unvisited_neighbors, new_moves = get_nearest_neighbors(graph, head, visited)
        for idx, unvisited_neighbor in enumerate(unvisited_neighbors):
            queue.append(unvisited_neighbor)
            visited.append(unvisited_neighbor)
            tmp_moves = moves_to_head
            tmp_moves += new_moves[idx]
            moves.append(tmp_moves)

    return None, None

def get_nearest_neighbors(graph, current_position, visited_positions):
    """ Return the positions that can be reached from the current_position.
    """
    total_rows = len(graph)
    total_columns = len(graph[0])
    moves = []
    positions = []

    current_height = get_height(graph, current_position)

    # Check if we can go up
    if current_position[0] > 0:
        up_position = (current_position[0]-1, current_position[1])
        if up_position not in visited_positions:
            up_height = get_height(graph, up_position)
            if up_height <= current_height+1:
                moves.append("^")
                positions.append(up_position)

    # Check if we can go right
    if current_position[1] < total_columns-1:
        right_position = (current_position[0], current_position[1]+1)
        if right_position not in visited_positions:
            right_height = get_height(graph, right_position)
            if right_height <= current_height+1:
                moves.append(">")
                positions.append(right_position)

    # Check if we can go down
    if current_position[0] < total_rows-1:
        down_position = (current_position[0]+1, current_position[1])
        if down_position not in visited_positions:
            down_height = get_height(graph, down_position)
            if down_height <= current_height+1:
                moves.append("v")
                positions.append(down_position)

    # Check if we can go left
    if current_position[1] > 0:
        left_position = (current_position[0], current_position[1]-1)
        if left_position not in visited_positions:
            left_height = get_height(graph, left_position)
            if left_height <= current_height+1:
                moves.append("<")
                positions.append(left_position)

    return positions, moves

def get_height(graph, position):
    """ Get height of position in the graph.
    """
    current_char = graph[position[0]][position[1]]
    if current_char == 'S':
        current_char = 'a'
    elif current_char == 'E':
        current_char = 'z'
    return ascii_lowercase.find(current_char)

def get_start_and_final_positions(graph):
    """ Return the starting and final position in the graph for the puzzle.
    """
    total_rows = len(graph)
    total_columns = len(graph[0])
    for row in range(total_rows):
        for column in range(total_columns):
            if graph[row][column] == "S":
                starting_position = (row, column)
            elif graph[row][column] == "E":
                final_postion = (row, column)
    return starting_position, final_postion

def part_one(inputs):
    """ Placeholder function to return result to first part of puzzle.
    """
    starting_position, final_postion = get_start_and_final_positions(inputs)
    return breadth_first_search(inputs, starting_position, final_postion)[1]

def find_all_positions(graph, char):
    """ Return all positions in the graph that match the char specified.
    """
    total_rows = len(graph)
    total_columns = len(graph[0])
    positions = []
    for row in range(total_rows):
        for column in range(total_columns):
            if graph[row][column] == char:
                positions.append((row, column))
    return positions

def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    _, final_postion = get_start_and_final_positions(inputs)
    starting_positions = find_all_positions(inputs, "a")
    steps = []
    for position in starting_positions:
        steps.append(breadth_first_search(inputs, position, final_postion)[1])
    return min([count for count in steps if count is not None])

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
