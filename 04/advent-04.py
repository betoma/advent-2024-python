import argparse

def parse_wordsearch(filename:str):
    with open(filename, "r+") as f:
        return [list(line.strip()) for line in f]


def get_start_coords(wordsearch:list[list[str]], letter: str):
    output_coords = []
    for i, row in enumerate(wordsearch):
        output_coords.extend([(i,j) for j, x in enumerate(row) if x == letter])
    return output_coords


def get_m(wordsearch:list[list[str]],x_coords:tuple[int]):
    test_diff = {
        (0,-1),
        (-1,0),
        (-1,-1),
        (-1,1),
        (1,-1),
        (0,1),
        (1,0),
        (1,1)
    }
    output = []
    for d in test_diff:
        if adj_m := find_follower(wordsearch, x_coords, d, "X"):
            output.append(adj_m)
    return output


def find_follower(wordsearch:list[list[str]],coords:tuple[int],diff:tuple[int],letter: str):
    if letter == "X":
        next_letter = "M"
    elif letter == "M":
        next_letter = "A"
    elif letter == "A":
        next_letter = "S"
    row, col = coords
    new_row = row + diff[0]
    if new_row <  0 or new_row >= len(wordsearch):
        return False
    new_col = col + diff[1]
    if new_col < 0 or new_col >= len(wordsearch[new_row]):
        return False
    if wordsearch[new_row][new_col] == next_letter:
        return ((new_row, new_col), diff)
    return False


def mas_check(wordsearch:list[list[str]],coords:tuple[int]):
    row, col = coords
    if row == 0 or row == len(wordsearch) - 1 or col == 0 or col == len(wordsearch[0]) - 1:
        return False
    corners = {
        "NE": wordsearch[row-1][col+1],
        "NW": wordsearch[row-1][col-1],
        "SE": wordsearch[row+1][col+1],
        "SW": wordsearch[row+1][col-1]
    }
    if any(x not in {"M","S"} for x in corners.values()):
        return False
    if corners["NE"] == corners["NW"]:
        matching_corner = "NW"
    elif corners["NE"] == corners["SE"]:
        matching_corner = "SE"
    else:
        return False
    if corners["NE"] == "M":
        other_letter = "S"
    else:
        other_letter = "M"
    for k, v in corners.items():
        if k not in {"NE", matching_corner}:
            if v != other_letter:
                return False
    return True
    

def part_one(input_file:str):
    wordsearch = parse_wordsearch(input_file)
    x_coords = get_start_coords(wordsearch,"X")
    m_coords = [m for x in x_coords for m in get_m(wordsearch, x)]
    a_coords = [next for coords, diff in m_coords if (next := find_follower(wordsearch,coords,diff,"M"))]
    s_coords = [next for coords, diff in a_coords if (next := find_follower(wordsearch,coords,diff,"A"))]
    return len(s_coords)


def part_two(input_file:str):
    wordsearch = parse_wordsearch(input_file)
    a_coords = get_start_coords(wordsearch, "A")
    return sum(mas_check(wordsearch,a) for a in a_coords)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Advent 2024 Day 4"
    )
    parser.add_argument("filename")
    args = parser.parse_args()
    print(part_one(args.filename))
    print(part_two(args.filename))