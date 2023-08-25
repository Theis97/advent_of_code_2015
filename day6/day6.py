import re


def run_instruction_part_one(grid: list[list[bool]], instruction: str, start: (int, int), end: (int, int)):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if instruction == "turn on":
                grid[i][j] = True
            elif instruction == "turn off":
                grid[i][j] = False
            else:
                grid[i][j] = not grid[i][j]


def run_instruction_part_two(grid: list[list[int]], instruction: str, start: (int, int), end: (int, int)):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if instruction == "turn on":
                grid[i][j] += 1
            elif instruction == "turn off":
                grid[i][j] -= 1
                if grid[i][j] < 0:
                    grid[i][j] = 0
            else:
                grid[i][j] += 2


if __name__ == '__main__':
    lights_part_one = [[False] * 1000 for i in range(1000)]
    lights_part_two = [[0] * 1000 for i in range(1000)]

    file = open("input.txt")

    instruction_regex = re.compile(r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

    for line in file:
        m = instruction_regex.match(line)
        instruction = m.groups()[0]
        start = (int(m.groups()[1]), int(m.groups()[2]))
        end = (int(m.groups()[3]), int(m.groups()[4]))

        run_instruction_part_one(lights_part_one, instruction, start, end)
        run_instruction_part_two(lights_part_two, instruction, start, end)

    num_lit = 0
    total_brightness = 0
    for i in range(1000):
        for j in range(1000):
            if lights_part_one[i][j]:
                num_lit += 1
            total_brightness += lights_part_two[i][j]

    print(f'Part 1 # lights lit: {num_lit}')
    print(f'Part 2 total brightness: {total_brightness}')
