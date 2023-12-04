MAX_VALS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def parse(data):
    total = 0
    counter = 0
    for line in data:
        print(line)
        counter += 1
        exceeded = False
        data1 = line.split(":")[1].split(";")
        print(data1)
        for dset in data1:
            data2 = dset.split(",")
            print(data2)
            for tmp_data in data2:
                col_val = tmp_data.split(" ")
                if int(col_val[1]) > MAX_VALS[col_val[2]]:
                    exceeded = True
        if not exceeded:
            total += counter
    return total

def main():
    raw_data = get_input()
    total = parse(raw_data)
    print(total)


if __name__ == "__main__":
    main()
