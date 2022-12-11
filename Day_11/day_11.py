#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 11, 2022.
"""
from os import path
from dataclasses import dataclass
import heapq

def read_file(file_path):
    """ Return contents of the specified file.
    """
    with open(file_path, encoding='UTF-8') as file:
        return file.read().splitlines(False)

class Monkeys:
    """ Class to represent all the Monkeys
    """
    def __init__(self, inputs):
        self.barrel = []
        for i in range((len(inputs)//7)+1):
            self.barrel.append(self.Monkey(i, inputs))
        self.common_multiple = self.test_divisor_common_multiple()

    @dataclass
    class Monkey:
        """ Class to represent each Monkey
        """
        def __init__(self, i, inputs):
            self.current_items = [int(item) for item in inputs[(i*7)+1][18:].split(",")]
            self.operator = inputs[(i*7)+2][23]
            self.operation = inputs[(i*7)+2][25:]
            self.test_divisor = int(inputs[(i*7)+3][21:])
            self.true_monkey = int(inputs[(i*7)+4][29:])
            self.false_monkey = int(inputs[(i*7)+5][30:])
            self.times_inspected = 0

    def test_divisor_common_multiple(self):
        """ Return the a common multiple for the test divisors used by all the monkeys
        """
        divisors = [monkey.test_divisor for monkey in self.barrel]
        lcm = divisors[0]
        for i in range(len(divisors)-1):
            lcm = lcm * divisors[i+1]
        return lcm

    def business_level(self):
        """ Return the current total monkey business level.
        """
        inspections = [monkey.times_inspected for monkey in self.barrel]
        two_largest = heapq.nlargest(2, inspections)
        return two_largest[0]*two_largest[1]

    def execute_rounds(self, rounds_to_run=1, staying_calm=True):
        """ Execute specified number of round of monkey business.
        """
        round_cnt = 0
        while round_cnt < rounds_to_run:
            for monkey in self.barrel:
                for item in monkey.current_items:
                    monkey.times_inspected += 1

                    if monkey.operation == "old":
                        number = item
                    else:
                        number = int(monkey.operation)

                    if monkey.operator == "*":
                        worry_level = item * number
                    elif monkey.operator == "+":
                        worry_level = item + number

                    if staying_calm:
                        worry_level = worry_level // 3
                    else:
                        worry_level = worry_level % self.common_multiple

                    if (worry_level % monkey.test_divisor) == 0:
                        self.barrel[monkey.true_monkey].current_items.append(worry_level)
                    else:
                        self.barrel[monkey.false_monkey].current_items.append(worry_level)

                monkey.current_items = []
            round_cnt +=1


def part_one(inputs):
    """ Placeholder function to return result to first part of puzzle.
    """
    monkeys = Monkeys(inputs)
    monkeys.execute_rounds(20)
    return monkeys.business_level()

def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    monkeys = Monkeys(inputs)
    staying_calm = False
    monkeys.execute_rounds(10000, staying_calm)
    return monkeys.business_level()

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
