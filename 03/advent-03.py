import argparse
import re


def part_one(input_file:str):
    with open(input_file, "r+") as f:
        content = f.read()
    total = 0
    for mat in re.finditer(r"mul\((-?\d{1,3}),(-?\d{1,3})\)", content):
        total += int(mat.group(1)) * int(mat.group(2))
    return total


def part_two(input_file:str):
    with open(input_file, "r+") as f:
        content = f.read()
    total = 0
    is_do = True
    for mat in re.finditer(r"(mul)\((-?\d{1,3}),(-?\d{1,3})\)|(do(?:n't)?)\(\)", content):
        if mat.group(1) == "mul" and is_do:
            total += int(mat.group(2)) * int(mat.group(3))
        elif mat.group(4) == "do":
            is_do = True
        elif mat.group(4) == "don't":
            is_do = False
    return total
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Advent 2024 Day 3"
    )
    parser.add_argument("filename")
    args = parser.parse_args()
    print(part_one(args.filename))
    print(part_two(args.filename))