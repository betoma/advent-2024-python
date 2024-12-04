import argparse
from collections import Counter

def read_input(filename:str):
    list_one = []
    list_two = []
    with open(filename, "r+") as f:
        for line in f:
            first, second = line.split()
            list_one.append(int(first))
            list_two.append(int(second))
    return list_one, list_two


def part_one(input_file:str):
    list_one, list_two = read_input(input_file)
    total = 0
    for one, two in zip(sorted(list_one),sorted(list_two)):
        total += abs(one - two)
    return total


def part_two(input_file:str):
    list_one, list_two = read_input(input_file)
    right_counter = Counter(list_two)
    total = 0
    for num in list_one:
        total += num * right_counter[num]
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Advent 2024 Day 1"
    )
    parser.add_argument("filename")
    args = parser.parse_args()
    print(part_one(args.filename))
    print(part_two(args.filename))
