def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def sort_dict(ind):
    myKeys = list(ind.keys())
    myKeys.sort(reverse=True)
    return {i: ind[i] for i in myKeys}


def main():
    raw_data = get_input()
    counter = 0
    tracker = {
        i: {"depth": {}, "value": 0}
        for i in range(0,len(raw_data))
    }
    for h in range(0, len(raw_data)):
        vals = [
            int(i)
            for i in raw_data[h].split()
        ]
        tracker[h]["depth"][0] = vals[0]
        found = False

        diff_count = 1
        while not found:
            diff_track = []
            for j in range(0,len(vals)-1):
                diff_track.append(vals[j+1]-vals[j])
            tracker[h]["depth"][diff_count] = diff_track[0]
            if len(set(diff_track)) == 1:
                found = True
            else:
                diff_count += 1
                vals = diff_track
        
        tracker[h]["depth"] = sort_dict(tracker[h]["depth"])
        sub_total = 0
        for _, value in tracker[h]["depth"].items():
            print(f"sub: {sub_total} - {value} = {sub_total - value}")
            sub_total = value - sub_total
        tracker[h]["value"] = sub_total
        counter += sub_total
        
    print(counter)


if __name__ == "__main__":
    main()
