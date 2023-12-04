def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def search(y, x, data):
    
    max_y = len(data) -1
    max_x = len(data[0]) -1
    # print(f"max_y: {max_y}, max_x: {max_x}")
    count_y = 2
    count_x = 2
    start_y = y-1
    start_x = x-1

    if y == 0:
        start_y = y
    elif y != max_y:
        count_y = 3

    if x == 0:
        start_x = x
    elif x != max_x:
        count_x = 3

    for y_cord in range(start_y, start_y+count_y):
        for x_cord in range(start_x, start_x+count_x):
            # print(f"y: {y_cord}, x: {x_cord}")
            if y_cord == y and x_cord == x:
                # print("original char, skipping....")
                continue
            char = data[y_cord][x_cord]
            # print(f"y: {y}, x: {x}, y_cord: {y_cord}, x_cord: {x_cord}, char: {char}")
            if not char.isdigit() and char != ".":
                return True
    return False
    


def main():
    raw_data = get_input()
    total = 0
    for y in range(0, len(raw_data)):
        ispart = 0
        for x in range(0, len(raw_data[0])):
            if raw_data[y][x] == "*":
                ispart = search(y, x, raw_data)
                total += ispart
    print(total)


if __name__ == "__main__":
    main()
