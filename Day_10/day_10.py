#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 10, 2022.
"""
from os import path

def read_file(file_path):
    """ Return contents of the specified file.
    """
    with open(file_path, encoding='UTF-8') as file:
        return file.read().splitlines(False)

def part_one(cpu_instructions):
    """ Placeholder function to return result to first part of puzzle.
    """
    sum_of_strengths = 0
    for i in range(6):
        sum_of_strengths += get_signal_strength(cpu_instructions, 20+(i*40))
    return sum_of_strengths

def get_signal_strength(cpu_instructions, during_cycle):
    """ Return the signal strength during the cycle specified.
    """
    return get_register_x_value(cpu_instructions, during_cycle) * during_cycle

def get_register_x_value(cpu_instructions, during_cycle):
    """ Return value in register x during the cycle specified.
    """
    registerx = 1
    current_cycle = 1
    current_line = 0
    while current_cycle < during_cycle:
        current_cpu_cmd = cpu_instructions[current_line]
        current_line +=1
        match current_cpu_cmd[:4]:
            case "addx":
                if (current_cycle + 2) <= during_cycle:
                    current_cycle += 2
                    registerx += int(current_cpu_cmd[5:])
            case "noop":
                current_cycle += 1
    return registerx

def part_two(cpu_instructions):
    """ Placeholder function to return result to second part of puzzle.
    """
    result = "\n"
    for row in range(6):
        result += get_crt_row(cpu_instructions, row)
    return result

def get_crt_row(cpu_instructions, row):
    """ Return string of CRT output for a given row and set of CPU instructions.
    """
    current_crt_row = ""
    for crt_pos in range(40):
        current_crt_cycle = crt_pos + 1 + (40 * row)
        sprite_pos = get_register_x_value(cpu_instructions, current_crt_cycle)
        if sprite_pos-1 <= crt_pos <= sprite_pos+1:
            current_crt_row += "#"
        else:
            current_crt_row += "."
    return current_crt_row + "\n"

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
