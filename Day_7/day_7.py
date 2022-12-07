#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 7, 2022.
"""
from os import path

class Directory:
    """ Object to represent each Directory
    """

    def __init__(self, name):
        self.name = name
        self.sub_directories = []
        self.files = []
        self.file_sizes = []

    def get_size(self):
        """ Return size of the current directory and all sub directories
        """
        size = sum(self.file_sizes)
        for sub_dir in self.sub_directories:
            size += sub_dir.get_size()
        return size

    def print_tree(self, prefix = ""):
        """ Print tree of directory structure. Not necesarry for puzzle, just practice.
        """
        print(prefix + "- " + self.name + " (dir)")
        for directory in self.sub_directories:
            directory.print_tree(prefix + "  ")
        for idx, single_file in enumerate(self.files):
            print(prefix + "  - " + single_file + " (file, size=" + str(self.file_sizes[idx]) + ")")


def read_file(file_path):
    """ Return contents of the specified file.
    """
    with open(file_path, encoding='UTF-8') as file:
        return file.read().splitlines(False)

def part_one(inputs):
    """ Placeholder function to return result to first part of puzzle.
    """
    root = Directory("/")
    root, _ = process_lines(root, inputs)
    sizes = find_small_directories(root, 100000)
    result = sum(sizes)
    return result

def find_small_directories(directory, size):
    """ Find if directory and sub directory sizes are less than the size
    specified, and return a list of those directory sizes.
    """
    sizes = []
    if directory.get_size() < size:
        sizes.append(directory.get_size())
    for sub_dir in directory.sub_directories:
        sizes.extend(find_small_directories(sub_dir, size))
    return sizes

def process_lines(current_directory, remaining_lines_to_process):
    """ Main function for processing commands/results in input file
    """
    start_count = False
    next_line = 0
    count = 0
    for count, line in enumerate(remaining_lines_to_process):
        if next_line == count:
            next_line += 1
            if line.find('$ cd ') != -1:
                start_count = False
                dir_to_go_to = line[5:]
                if dir_to_go_to == "..":
                    return current_directory, count+1
                if dir_to_go_to == "/" and current_directory.name != "/":
                    return current_directory, count
                for idx, sub_directory in enumerate(current_directory.sub_directories):
                    if sub_directory.name == dir_to_go_to:
                        current_directory.sub_directories[idx], count_add = \
                        process_lines(sub_directory, remaining_lines_to_process[count+1:])
                        next_line += count_add
            elif line.find('$ ls') != -1:
                start_count = True
            elif start_count and has_numbers(line):
                space_index = line.find(' ')
                current_directory.files.append(line[space_index+1:])
                size = int(line[0:space_index])
                current_directory.file_sizes.append(size)
            elif start_count and not has_numbers(line):
                space_index = line.find(' ')
                dir_name = line[space_index+1:]
                if dir_name not in [sub_dir.name for sub_dir in current_directory.sub_directories]:
                    new_directory = Directory(dir_name)
                    current_directory.sub_directories.append(new_directory)
    return current_directory, count

def has_numbers(string_in):
    """ Return true if string provided contains numbers
    """
    return any(char.isdigit() for char in string_in)

def find_smallest_big_enough_directory(directory, size):
    """ Find if directory and sub directories are larger than specified size,
    return a list of those directory sizes if so.
    """
    sizes = []
    if directory.get_size() >= size:
        sizes.append(directory.get_size())
    for sub_dir in directory.sub_directories:
        sizes.extend(find_smallest_big_enough_directory(sub_dir, size))
    return sizes

def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    root = Directory("/")
    root, _ = process_lines(root, inputs)
    space_available = 70000000 - root.get_size()
    space_needed = 30000000 - space_available
    result = min(find_smallest_big_enough_directory(root, space_needed))
    return result

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
