import re

def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def get_number(data):
    for letter in data:
        print(letter)
        if re.match(r"[0-9]", letter):
            return letter
        

def main():
    raw_data = get_input()
    total = 0
    for line in raw_data:
        first = get_number(line)
        last = get_number(line[::-1])
        value = int(f'{first}{last}')
        print(value)
        total += value
    
    print(f"Puzzle answer: {total}")


if __name__ == "__main__":
    main()
