import re


def part_one(filename: str) -> int:
    file = open(filename)

    num_nice_strings = 0
    for line in file:
        if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
            continue

        double_candidate = ""
        has_double = False
        num_vowels = 0
        for char in line:
            if char in "aeiou":
                num_vowels += 1
            if char == double_candidate:
                has_double = True
            else:
                double_candidate = char

        if has_double and num_vowels >= 3:
            num_nice_strings += 1

    file.close()
    return num_nice_strings


def part_two(filename: str) -> int:
    file = open(filename)

    num_nice_strings = 0
    double_pair_regex = re.compile(r".*(..).*\1")
    interrupted_repeat_regex = re.compile(r".*(.).\1")

    for line in file:
        if (double_pair_regex.match(line) is not None
                and interrupted_repeat_regex.match(line) is not None):
            num_nice_strings += 1

    file.close()
    return num_nice_strings


if __name__ == '__main__':
    print(f'# nice strings for part 1: {part_one("input.txt")}')
    print(f'# nice strings for part 2: {part_two("input.txt")}')
