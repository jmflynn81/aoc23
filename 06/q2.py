import math


def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def get_int(data):
    return int(data.split(":")[1].replace(" ", ""))


def main():
    raw_data = get_input()
    time = get_int(raw_data[0])
    record = get_int(raw_data[1])

    val = (-math.sqrt((time**2)-(4*record))+time)/2

    round_err = 1
    if time%2 == 1:
        round_err = round_err * -1

    beat = (time - math.ceil(val)*2) + round_err
    print(f"Beat: {beat}")


if __name__ == "__main__":
    main()
