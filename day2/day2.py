from functools import reduce

if __name__ == '__main__':
    file = open("input.txt")

    total_wrapping_paper: int = 0
    total_ribbon_length: int = 0
    for line in file:
        dimensions = line.strip().split('x')
        l, w, h = [int(value) for value in dimensions]

        # Calculate wrapping paper needed for part 1
        face_areas: list[int] = [l * w, w * h, l * h]
        min_face_area: int = min(face_areas)
        surface_area: int = 2 * reduce(lambda x, y: x + y, face_areas)
        total_wrapping_paper += surface_area + min_face_area

        # Calculate ribbon needed for part 2
        volume: int = l * w * h
        perimeters: list[int] = [(2 * l) + (2 * w), (2 * w) + (2 * h), (2 * l) + (2 * h)]
        min_perimeter = min(perimeters)
        total_ribbon_length += volume + min_perimeter

    file.close()
    print(f'Total wrapping paper needed: {total_wrapping_paper} sq ft')
    print(f'Total ribbon length needed: {total_ribbon_length} ft')
