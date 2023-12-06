def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def get_list(data):
    return [
        int(time)
        for time in data.split(":")[1].split()
    ]


def main():
    raw_data = get_input()
    times = get_list(raw_data[0])
    records = get_list(raw_data[1])

    total = 1
    for i in range(0, len(times)):
        print(f"time: {times[i]}")
        beat = 0
        for j in range(0, times[i]):
            new_time = j*(times[i]-j)
            print(f"button hold: {j}, remain: {times[i]-j}, new time: {new_time}")
            if new_time > records[i]:
                beat += 1
        print(f"Beat: {beat}")
        total *= beat
        print(f"total: {total}")
    print(total)


if __name__ == "__main__":
    main()
