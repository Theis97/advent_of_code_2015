import re

if __name__ == '__main__':
    file = open("input.txt")

    code_length = 0
    memory_length = 0
    encoded_length = 0
    for line in file:
        string = line.strip()
        code_length += len(string)
        substituted_string = re.sub(r'\\x..|\\\\|\\"', '_', string)
        memory_length += len(substituted_string) - 2
        encoded_length += len(string) + string.count('"') + string.count('\\') + 2

    print(f'Part 1 answer: {code_length - memory_length}')
    print(f'Part 2 answer: {encoded_length - code_length}')
