import re

def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def search(y, x, data):
    
    max_y = len(data) -1
    max_x = len(data[0]) -1
    # print(f"max_y: {max_y}, max_x: {max_x}")

    start_y = y-1
    if start_y < 0:
        start_y = 0

    start_x = x-3
    if start_x < 0:
        start_x = 0
    
    end_y = y+1
    if end_y > max_y:
        end_y = max_y
    
    end_x = x+3
    if end_x > max_x:
        end_x = max_x

    gears = 0
    ltv = 1
    rtv = 1
    lmv = 1
    rmv = 1
    lbv = 1
    rbv = 1
    if start_y != y:
        top_check = data[start_y][start_x:end_x+1]
        
        for tc in re.finditer("\d+", top_check):
            # print(list(range(tc.start(), tc.end())))
            if tc.start == 2 or tc.end() == 3:
                ltv = int(tc.group())
                gears += 1
            if tc.start() in [3, 4] or tc.end() in [4, 5]: # <----start here tomorrow
                rtv = int(tc.group())
                gears += 1
                if ltv == rtv:
                    rtv = 1
                    gears -= 1
            
    mid_check = data[y][start_x:end_x+1]
    for mc in re.finditer("\d+", mid_check):
        if mc.end() == 3:
            lmv = int(mc.group())
            gears += 1
        if mc.start() == 4:
            rmv = int(mc.group())
            gears += 1

    if end_y != y:
        bottom_check = data[end_y][start_x:end_x+1]
        for bc in re.finditer("\d+", bottom_check):
            # print(list(range(bc.start(), bc.end())))
            if bc.start() == 2 or bc.end() == 3:
                lbv = int(bc.group())
                gears += 1
            if bc.start() in [3, 4] or bc.end() in [4, 5]:
                rbv = int(bc.group())
                gears += 1
                if lbv == rbv:
                    rbv = 1
                    gears -= 1

                

    # print(top_check, tv)
    # print(mid_check, mv)
    # print(bottom_check, bv)
    # print()
    print(f"ltv: {ltv}, rtv: {rtv}, lmv: {lmv}, rmv: {rmv}, lbv: {lbv}, rbv: {rbv}, gears: {gears} [{top_check}][{mid_check}][{bottom_check}]")
    # print(f"top_values: {top_check}, found: {tv}")
    # print(f"lmd_values: {mid_check}, found: {lmv}")
    # print(f"rmd_values: {mid_check}, found: {rmv}")
    # print(f"bot_values: {bottom_check}, found: {bv}, ({bc.start()},{bc.end()})")
    # print()
    product = rtv * ltv * rmv * lmv * rbv * lbv
    if product == 1 or gears != 2:    
        return 0
    else:
        return product


def main():
    raw_data = get_input()
    total = 0
    for y in range(0, len(raw_data)):
        ispart = 0
        for x in range(0, len(raw_data[0])):
            if raw_data[y][x] == "*":
                ispart = search(y, x, raw_data)
                total += ispart
    print(total)


if __name__ == "__main__":
    main()

# 0123456
# 999.999
# 999*999
# 999.999

# ...
# .*.
# ...

# -1,-1;-1,0;-1,1