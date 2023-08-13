if __name__ == '__main__':
    file = open("input.txt")
    input_text = file.read()
    file.close()

    floor = 0
    has_entered_basement = False
    for idx, char in enumerate(input_text):
        if char == '(':
            floor += 1
        if char == ')':
            floor -= 1
        if floor == -1 and not has_entered_basement:
            print(f'Entered basement at position: {idx + 1}')
            has_entered_basement = True

    print(f'Final floor number: {floor}')
