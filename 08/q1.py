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
    cur_pos = "AAA"
    step_pos_max = len(commands)
    steps = 0
    while cur_pos != "ZZZ":
        # sleep(1)
        command = commands[steps % step_pos_max]
        print(command)
        print(cur_pos)
        if command == "L":
            cur_pos = parsed_data[cur_pos][0]
        else:
            cur_pos = parsed_data[cur_pos][1]
        steps +=1
    
    print(steps)



if __name__ == "__main__":
    main()

# 