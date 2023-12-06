import re


def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def sort_dict(ind):
    myKeys = list(ind.keys())
    myKeys.sort()
    return {i: ind[i] for i in myKeys}


def parse(data):
    seeds = {}
    sections = {}
    pointer = ""
    for line in data:
        if not re.match("^\d", line.split(":")[0]):
            pointer = line.split(":")[0]
            if pointer == "seeds":
                seedy = [int(seed) for seed in line.split(":")[1].split()]
                seeds = {seedy[i]: (seedy[i]+seedy[i+1])-1 for i in range(0, len(seedy), 2)}
                seeds = sort_dict(seeds)
            elif pointer != "":
                sections[pointer] = {}
            continue
        else:
            values = line.split()
            sections[pointer][int(values[1])] = {"destination":int(values[0]), "range": int(values[2])}
    
    for section in sections:
        sections[section] = sort_dict(sections[section])
    locations = {}
    
    for section in sections:
        previous_end = 0
        locations[section] = {}
        for location in sections[section]:
            if location > previous_end:
                locations[section][previous_end] = {"destination": previous_end, "range": location}
            locations[section][location] = sections[section][location]
            previous_end = sections[section][location]["range"] + location
    
    for location in locations:
        num_locations = len(locations[location])-1
        last_location_key = list(locations[location])[num_locations]
        ranger = locations[location][last_location_key]["range"]
        locations[location][last_location_key+ranger] = {"destination": last_location_key+ranger, "range": 99999999999}

    return seeds, locations


def breakout(start,end, loc):
    retdict = {}
    for this_start in loc:
        this_range = loc[this_start]["range"]
        this_dest = loc[this_start]["destination"]
        this_end = this_range + this_start
        if start >= this_end or end < this_start:
            continue
            
        if end >= this_end:
            retdict.update(breakout(this_end, end, loc))
            end = this_end-1
        retdict[start - this_start+this_dest] = end - this_start+this_dest
        break
    return(retdict)


def get_best(seeds, data):
    lowest = 9999999999999999999999999999999
    current = {"start": 0, "end": 0}
    for key, value in seeds.items():
        current = {key: value}
        for location in data:
            current_temp = {}
            for start, end in current.items():
                current_temp.update(breakout(start, end, data[location]))
            current = current_temp
        current_list = list(current.keys())
        current_list.sort()
        if current_list[0] < lowest:
            lowest = current_list[0]
    print(lowest)


def main():
    raw_data = get_input()
    seeds, parsed_data = parse(raw_data)
    get_best(seeds, parsed_data)


if __name__ == "__main__":
    main()
