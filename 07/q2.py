import json

CARD_MAP = {
    "T": 10,
    "J": 1,
    "Q": 11,
    "K": 12,
    "A": 13
}
STRENGTH_MAP = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g"
}
CARD_LOCATION_MAP = {
    "J": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H",
    "9": "I",
    "T": "J",
    "Q": "K",
    "K": "L",
    "A": "M",
}


def get_input():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
    return raw_data


def sort_dict(ind):
    myKeys = list(ind.keys())
    myKeys.sort()
    return {i: ind[i] for i in myKeys}


def parse(data):
    card_map = {}
    for card_data in data:
        cards = card_data.split()[0]
        bid = int(card_data.split()[1])
        card_value_list = []
        card_placement_id = ""
        for card in cards:
            if card not in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                card_value_list.append(CARD_MAP[card])
            else:
                card_value_list.append(int(card))
        
        for card in cards:
            card_placement_id += CARD_LOCATION_MAP[card]
        
        set_cards = list(set(cards))
        joker = False
        if "J" in set_cards:
            joker = True
        card_len = len(set_cards)
        if card_len == 1:
            card_strength = 7
        elif card_len == 2:
            breakdown = get_quantities(cards)
            if 4 in list(breakdown.values()):
                if joker:
                    card_strength = 7
                else:
                    card_strength = 6
            else:
                if joker:
                    card_strength = 7
                else:
                    card_strength = 5
        elif card_len == 3:
            breakdown = get_quantities(cards)
            if 3 in list(breakdown.values()):
                if joker:
                    card_strength = 6
                else:
                    card_strength = 4
            else:
                if joker:
                    if breakdown["J"] == 1:
                        card_strength = 5
                    else:
                        card_strength = 6
                else:
                    card_strength = 3
        elif card_len == 4:
            if joker:
                card_strength = 4
            else:
                card_strength = 2
        elif card_len == 5:
            if joker:
                card_strength = 2
            else:
                card_strength = 1
        card_placement_id = STRENGTH_MAP[card_strength] + card_placement_id
        card_map[card_placement_id] = {"card": cards, "bid": bid, "values": card_value_list, "strength": card_strength}
    return card_map


def get_quantities(cards):
    return {i:cards.count(i) for i in cards}


def work(card_map):
    
    card_map = sort_dict(card_map)
    card_list = list(card_map.keys())
    total = 0
    for position in range(0, len(card_list)):
        total += (position + 1)*card_map[card_list[position]]["bid"]
    
    print(total)


def main():
    raw_data = get_input()
    card_map = parse(raw_data)
    work(card_map)
    


if __name__ == "__main__":
    main()
