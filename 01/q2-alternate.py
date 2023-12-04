import re

LIST = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
REPEAT = {
    "nei": "neei",
    "eei": "eeei",
    "won": "woon",
    "vei": "veei",
    "eni": "enni",
    "htw": "httw",
    "hth": "htth"
}


def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def normalise(data):
    for letter in REPEAT:
        data = data.replace(letter, REPEAT[letter])
    for word in LIST:
        data = re.sub(word, LIST[word], data)
    return data


def get_number(data, direction):    
    for letter in data[::direction]:
        if re.match(r"[0-9]", letter):
            return letter


def main():
    raw_data = get_input()
    total = 0
    for line in raw_data:
        nline = normalise(line)
        first = get_number(nline, 1)
        last = get_number(nline, -1)
        value = int(f'{first}{last}')
        total += value
    
    print(f"Puzzle answer: {total}")


if __name__ == "__main__":
    main()
