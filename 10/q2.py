D_MAP = {
    "F": {"yb": [0,1], "ya": None, "xl": None, "xr": [1,0]},
    "|": {"yb": [-1,0], "ya": [1,0], "xl": None, "xr": None},
    "J": {"yb": None, "ya": [0,-1], "xl": [-1,0], "xr": None},
    "L": {"yb": None, "ya": [0,1], "xl": None, "xr": [-1,0]},
    "7": {"yb": [0,-1], "ya": None, "xl": [1,0], "xr": None},
    "-": {"yb": None, "ya": None, "xl": [0,1], "xr": [0,-1]}
}


def get_input():
    with open("testinput2.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data



def main():
    raw_data = get_input()
    s = []
    for y in range(0,len(raw_data)):
        for x in range(0, len(raw_data[y])):
            if raw_data[y][x] == "S":
                s = [y,x]
                break
        if len(s) == 2:
            break
    
    n_move = [1, 0]
    loop = False
    # steps = 0
    cat = {
        y: []
        for y in range(0,len(raw_data))
    }
    # cat[s[0]].append(s[1])
    move = ""
    while not loop:
        # cat[s[0]].append(s[1])
        # steps += 1
        # print(s)
        # print(raw_data[s[0]][s[1]])
        if n_move[0] != 0:
            if n_move[0] == 1:
                move = "ya"
            else:
                move = "yb"
            # cat[s[0]].append(s[1])
        elif n_move[1] != 0:
            if n_move[1] == 1:
                move = "xl"
            else:
                move = "xr"
        s[0] = s[0] + n_move[0]
        s[1] = s[1] + n_move[1]

        pipe = raw_data[s[0]][s[1]]
        # if pipe != "-":
        cat[s[0]].append(s[1])
        # print(pipe)
        if pipe == "S":
            loop = True
        else:
            n_move = D_MAP[pipe][move]
            if n_move == None:
                print("fuck")
                break
    
    total = 0
    
    for y in cat:
        print(y)
        inside = False
        for x in range(0, len(raw_data[0])):
            char = raw_data[y][x]
            
            if x in cat[y]:
                if char not in ["-"]:  
                    inside = not inside
            else:
                
                if inside:
                    total += 1
            print(y, x, char, inside)
    
    print(total)
        
    
    # print(int(steps/2))
        


    



if __name__ == "__main__":
    main()
