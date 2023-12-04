def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def main():
    raw_data = get_input()
    total = 0
    
    for line in raw_data:
        data = line.split(":")[1].split("|")
        winners = set([eval(i) for i in data[0].split()])
        mynums = set([eval(i) for i in data[1].split()])
        num_win = len(winners.intersection(mynums))
        if num_win > 0:
            total += 2**(num_win-1)
    print(total)




if __name__ == "__main__":
    main()
