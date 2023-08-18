def get_next_position(position: (int, int), direction: str) -> (int, int):
    if direction == '^':
        return position[0], position[1] + 1
    if direction == 'v':
        return position[0], position[1] - 1
    if direction == '>':
        return position[0] + 1, position[1]
    if direction == '<':
        return position[0] - 1, position[1]


def track_house_visits(directions: str, num_santas: int) -> int:
    # track each santa/robo-santa on a cartesian coordinate grid
    # east/west is +x/-x, north/south is +y/-y
    positions: list[(int, int)] = [(0, 0)] * num_santas
    turn: int = 0
    visited_houses: {(int, int)} = {(0, 0)}

    for char in directions:
        next_position = get_next_position(positions[turn], char)
        visited_houses.add(next_position)
        positions[turn] = next_position
        turn = (turn + 1) % num_santas

    return len(visited_houses)


if __name__ == '__main__':
    file = open("input.txt")
    input_text = file.read()
    file.close()

    print(f'Part 1 houses visited: {track_house_visits(input_text, 1)}')
    print(f'Part 2 houses visited: {track_house_visits(input_text, 2)}')
