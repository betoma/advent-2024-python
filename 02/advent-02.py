import argparse

def parse_input(filename:str):
    with open(filename, "r+") as f:
        reports = [[int(x) for x in line.split()] for line in f]
    return reports


def is_safe(report:list[int]):
    diff_list = [n - report[i+1] for i, n in enumerate(report[:-1])]
    if not all(n > 0 for n in diff_list) and not all(n < 0 for n in diff_list):
        return False
    if any(abs(n) > 3 for n in diff_list):
        return False
    return True


def problem_dampener(report: list[int]):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False


def part_one(input_file:str):
    reports = parse_input(input_file)
    return sum(is_safe(r) for r in reports)


def part_two(input_file:str):
    reports = parse_input(input_file)
    return sum(problem_dampener(r) for r in reports)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Advent 2024 Day 2"
    )
    parser.add_argument("filename")
    args = parser.parse_args()
    print(part_one(args.filename))
    print(part_two(args.filename))