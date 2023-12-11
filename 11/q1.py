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
    y_str = raw_data[expand_y[0]]
    expand_y.sort(reverse=True)
    for y in expand_y:
        raw_data.insert(y, y_str)
    expand_x = []
    for x in range(0, len(raw_data[0])):
        tmp_str = ""
        for y in range(0, len(raw_data)):
            tmp_str += raw_data[y][x]
        if "#" not in tmp_str:
            expand_x.append(x)
    expand_x.sort(reverse=True)
    for x in expand_x:
        for y in range(0,len(raw_data)):
            raw_data[y] = raw_data[y][:x] + "." + raw_data[y][x:]
    
    for y in raw_data:
        print(y)
    # cat = {
    #     y:[]
    #     for y in range(0, len(raw_data))
    # }
    coords = []
    for y in range(0, len(raw_data)):
        for x in range(0, len(raw_data[y])):
            if raw_data[y][x] == "#":
                # cat[y].append(x)
                coords.append([y, x])

    print(coords)
    num_coords = len(coords)
    pairs_vals = []
    for _ in range(0, num_coords):
        cur = coords.pop()
        for coord in coords:
            val = (abs(cur[0] - coord[0])) + (abs(cur[1] - coord[1]))
            print(f"distance between {cur} and {coord} is {val}")
            pairs_vals.append(val)
    
    print(sum(pairs_vals))


        

if __name__ == "__main__":
    main()
