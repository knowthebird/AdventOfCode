#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 21, 2022.
"""
from dataclasses import dataclass
from decimal import Decimal
from os import path

class Monkeys:
    """ Class to represent all the Monkeys
    """
    def __init__(self, inputs):
        self.barrel = []
        for line in inputs:
            split_line = line.split(' ')
            name = split_line[0][:-1]
            friends = []
            if len(split_line) == 2:
                number = int(split_line[1])
                operation = None
            elif len(split_line) == 4:
                number = None
                operation = split_line[2]
                friends.append(split_line[1])
                friends.append(split_line[3])

            self.barrel.append(self.Monkey(name, number, operation, friends))

    @dataclass
    class Monkey:
        """ Class to represent each Monkey
        """
        def __init__(self, name, number, operation, friends):
            self.name = name
            self.number = number
            self.operation = operation
            self.friends = friends

    def get_number(self, monkey_name):
        """ Returns the number for a monkey with a given name.
            If there is no number, calculates it.
        """
        for monkey in self.barrel:
            if monkey.name == monkey_name:
                if monkey.number is not None:
                    return monkey.number
                friend_one_number = self.get_number(monkey.friends[0])
                friend_two_number = self.get_number(monkey.friends[1])
                if monkey.operation == "+":
                    return Decimal(friend_one_number) + Decimal(friend_two_number)
                if monkey.operation == "-":
                    return Decimal(friend_one_number) - Decimal(friend_two_number)
                if monkey.operation == "*":
                    return Decimal(friend_one_number) * Decimal(friend_two_number)
                if monkey.operation == "/":
                    return Decimal(friend_one_number) / Decimal(friend_two_number)
        return None

    def get_human_number(self):
        """ Return the value the human would need to yell
        to make the values returned by each of roots friends equal.
        """
        for monkey in self.barrel:
            if monkey.name == "root":
                friends = monkey.friends

        humn_num = 0
        for monkey in self.barrel:
            if monkey.name == "humn":
                monkey.number = humn_num
        lhs_num = self.get_number(friends[0])
        rhs_num = self.get_number(friends[1])
        first_diff = Decimal(lhs_num) - Decimal(rhs_num)
        ans_one = lhs_num

        humn_num = 1
        for monkey in self.barrel:
            if monkey.name == "humn":
                monkey.number = humn_num
        ans_two = self.get_number(friends[0])

        diff_change_rate = ans_two - ans_one

        humn_num = int(Decimal(first_diff) / Decimal(-diff_change_rate))

        return humn_num

def read_file(file_path):
    """ Return contents of the specified file.
    """
    with open(file_path, encoding='UTF-8') as file:
        return file.read().splitlines(False)

def part_one(inputs):
    """ Placeholder function to return result to first part of puzzle.
    """
    monkeys = Monkeys(inputs)
    return monkeys.get_number("root")

def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    monkeys = Monkeys(inputs)
    return monkeys.get_human_number()

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    print("Part One Sample: " + str(part_one(inputs)))
    print("Part Two Sample: " + str(part_two(inputs)))
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
