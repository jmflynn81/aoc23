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


def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def get_number(data, direction):
    first_counter = 9999

    for word in LIST:
        tmp_data = re.sub(word, LIST[word], data)

        counter = 0
        for tmp_last in tmp_data[::direction]:
            if re.match(r"[0-9]", tmp_last):
                break
            counter += 1
        
        if counter <= first_counter:
            first = tmp_last
            first_counter = counter

    return first
        

def main():
    raw_data = get_input()
    total = 0
    for line in raw_data:
        first = get_number(line, 1)
        last = get_number(line, -1)
        value = int(f'{first}{last}')
        total += value
    
    print(f"Puzzle answer: {total}")


if __name__ == "__main__":
    main()
