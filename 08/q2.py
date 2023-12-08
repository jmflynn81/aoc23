from time import sleep


def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def main():
    raw_data = get_input()
    commands = raw_data.pop(0)
    raw_data.pop(0)
    parsed_data = {
        line.split("=")[0].strip():[line.split("=")[1].strip()[1:4], line.split("=")[1].strip()[6:9]]
        for line in raw_data
    }
    cur_pos = {}
    for key in parsed_data.keys():
        if key[2] == "A":
            cur_pos[key] = 1
    step_pos_max = len(commands)
    print(len(cur_pos))
    list_step = []
    for pos in cur_pos:
        print(parsed_data[pos])
        steps = 0
        while pos[2] != "Z":
            command = commands[steps % step_pos_max]
            if command == "L":
                command = 0
            else:
                command = 1
            pos = parsed_data[pos][command]
            steps +=1
        list_step.append(steps)

    total = 1

    tracker = {
        i:i
        for i in list_step
    }

    def factorize(num):
        return [n for n in range(1, num + 1) if num % n == 0]

    
    for i in list_step:
        tracker[i] = factorize(i)
        tracker[i].pop()

    factl = list(set.union(
        set(tracker[list_step[0]]), 
        set(tracker[list_step[1]]),
        set(tracker[list_step[2]]),
        set(tracker[list_step[3]]),
        set(tracker[list_step[4]]),
        set(tracker[list_step[5]])
        ))
    for vals in factl:
        total *= vals
    
    print(total)


if __name__ == "__main__":
    main()
