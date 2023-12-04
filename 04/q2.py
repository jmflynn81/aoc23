def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def main():
    raw_data = get_input()
    total = 0
    tracker = {
        i:1
        for i in range(0, len(raw_data))
    }
    print(tracker)
    for position in range(0, len(raw_data)):
        data = raw_data[position].split(":")[1].split("|")
        winners = set([eval(i) for i in data[0].split()])
        mynums = set([eval(i) for i in data[1].split()])
        num_win = len(winners.intersection(mynums))
        
        if num_win > 0:
            
            print(f"position: {position}, cards: {num_win}")
            for i in range(position+1, position+num_win+1):
                print(tracker)
                tracker[i] += tracker[position]
            

    print(tracker)
    print(sum(tracker.values()))



if __name__ == "__main__":
    main()
