import re


def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def parse(data):
    seeds = []
    sections = {
        "seed-to-soil map": {},
        "soil-to-fertilizer map": {},
        "fertilizer-to-water map": {},
        "water-to-light map": {},
        "light-to-temperature map": {},
        "temperature-to-humidity map": {},
        "humidity-to-location map": {}
    }
    pointer = ""
    for line in data:
        if not re.match("^\d", line.split(":")[0]):
            pointer = line.split(":")[0]
            if pointer == "seeds":
                seeds = [
                    int(seed)
                    for seed in line.split(":")[1].split()
                ]
                seeds.sort()
            continue
        else:
            values = line.split()
            sections[pointer][int(values[1])] = {"destination":int(values[0]), "range": int(values[2])}
    for section in sections:
        myKeys = list(sections[section].keys())
        myKeys.sort()
        sorted_dict = {i: sections[section][i] for i in myKeys}
        sections[section] = sorted_dict

    return seeds, sections


def get_destination(seeds, data):
    loc = 9999999999999999
    for seed in seeds:
        print()
        for section in data:
            print(f"{seed}, ", end="")
            for range in data[section]:
                if seed >= range and seed < range + data[section][range]["range"]:

                    seed = seed - range + data[section][range]["destination"]
                    break
        if seed < loc:
            loc = seed
    print()
    print(loc)


def main():
    raw_data = get_input()
    seeds, parsed_data = parse(raw_data)
    destination = get_destination(seeds, parsed_data)



if __name__ == "__main__":
    main()
