import hashlib


def find_key_suffix(key_prefix: str, num_leading_zeros: int) -> int:
    suffix: int = 1

    while True:
        to_hash = key_prefix + str(suffix)
        result = hashlib.md5(to_hash.encode())
        if result.hexdigest()[:num_leading_zeros] == '0' * num_leading_zeros:
            break
        suffix += 1

    return suffix


if __name__ == '__main__':
    file = open("input.txt")
    input_text = file.read()
    file.close()

    print(f'Part 1 answer: {find_key_suffix(input_text, 5)}')
    print(f'Part 2 answer: {find_key_suffix(input_text, 6)}')
