EXPANSION = 1000000

def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def main():
    raw_data = get_input()
    expand_y = [
        y
        for y in range(0, len(raw_data))
        if "#" not in raw_data[y]
    ]
    expand_x = []
    for x in range(0, len(raw_data[0])):
        tmp_str = ""
        for y in range(0, len(raw_data)):
            tmp_str += raw_data[y][x]
        if "#" not in tmp_str:
            expand_x.append(x)
    
    coords = []
    for y in range(0, len(raw_data)):
        for x in range(0, len(raw_data[y])):
            if raw_data[y][x] == "#":
                coords.append([y, x])

    num_coords = len(coords)
    pairs_vals = []
    for _ in range(0, num_coords):
        cur = coords.pop()
        for coord in coords:
            y_vals = [cur[0], coord[0]]
            y_vals.sort()
            y_extra_len = len(set.intersection(set(list(range(y_vals[0],y_vals[1]))), set(expand_y)))
            y_extra = (y_extra_len*EXPANSION)-y_extra_len
            x_vals = [cur[1], coord[1]]
            x_vals.sort()
            x_extra_len = len(set.intersection(set(list(range(x_vals[0],x_vals[1]))), set(expand_x)))
            x_extra = (x_extra_len*EXPANSION)-x_extra_len
            # print(f"cur: {cur}, coord: {coord}, x_vals: {x_vals}, x_extra: {x_extra}, y_vals: {y_vals}, y_extra: {y_extra}")
            val = (abs(cur[0] - coord[0])+y_extra) + (abs(cur[1] - coord[1])+x_extra)
            pairs_vals.append(val)
    print(sum(pairs_vals))
        

if __name__ == "__main__":
    main()
