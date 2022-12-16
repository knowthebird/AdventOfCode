#!/usr/bin/env python3
""" Module for AdventOfCode puzzle, Day 13, 2022.
"""
from os import path
import json

def read_file(file_path):
    """ Return contents of the specified file.
    """
    data = []
    with open(file_path, encoding='UTF-8') as file:
        for line in file:
            try:
                data.append(json.loads(line))
            except json.decoder.JSONDecodeError:
                pass # Still works even with the value errors
    return data

def part_one(inputs):
    """ Placeholder function to return result to first part of puzzle.
    """
    total_pairs_of_packets = int(len(inputs)/2)
    results = []
    for pair_idx in range(1,total_pairs_of_packets+1):
        left_packet = inputs[(pair_idx*2)-2]
        right_packet = inputs[(pair_idx*2)-1]
        if in_correct_order(left_packet, right_packet) == "yes":
            results.append(pair_idx)
    return sum(results)

def in_correct_order(left_packet, right_packet):
    """ Return if the left (first) packet should be left of (before) the right packet in order.
    """
    return_value = "continue"
    if (isinstance(left_packet, list) and isinstance(right_packet, list)):
        left_len = len(left_packet)
        right_len = len(right_packet)
        for idx in range(min([left_len, right_len])):
            return_value = in_correct_order(left_packet[idx], right_packet[idx])
            if return_value != "continue":
                break
        if return_value == "continue":
            if left_len < right_len:
                return_value = "yes"
            elif left_len > right_len:
                return_value = "no"
    elif (isinstance(left_packet, int) and isinstance(right_packet, int)):
        return_value = "continue"
        if left_packet < right_packet:
            return_value = "yes"
        elif left_packet > right_packet:
            return_value = "no"
    elif (isinstance(left_packet, list) and isinstance(right_packet, int)):
        new_right_packet = [right_packet]
        return_value = in_correct_order(left_packet, new_right_packet)
    elif (isinstance(left_packet, int) and isinstance(right_packet, list)):
        new_left_packet = [left_packet]
        return_value = in_correct_order(new_left_packet, right_packet)

    return return_value

def part_two(inputs):
    """ Placeholder function to return result to second part of puzzle.
    """
    divider_packets = [[[2]], [[6]]]
    for packet in divider_packets:
        inputs.append(packet)

    ordered_packets = []
    for new_packet in inputs:
        if len(ordered_packets) == 0:
            ordered_packets.append(new_packet)
        else:
            added = False
            for idx, existing_packet in enumerate(ordered_packets):
                if not added:
                    if in_correct_order(new_packet, existing_packet) == "yes":
                        ordered_packets.insert(idx,new_packet)
                        added = True
            if not added:
                ordered_packets.append(new_packet)

    final_divider_indices = []
    for divider in divider_packets:
        for idx, existing_packet in enumerate(ordered_packets):
            if existing_packet == divider:
                final_divider_indices.append(idx+1)

    decoder_key = final_divider_indices[0]*final_divider_indices[1]
    return decoder_key

def main():
    """ Main function to read inputs and pass to placeholder functions.
    """
    inputs = read_file(path.splitext(__file__)[0]+'_sample.txt')
    inputs = read_file(path.splitext(__file__)[0]+'_input.txt')
    print("Part One: " + str(part_one(inputs)))
    print("Part Two: " + str(part_two(inputs)))

if __name__ == '__main__':
    main()
