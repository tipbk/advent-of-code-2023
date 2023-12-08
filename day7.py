data = open('day7.txt', 'r').read().split('\n')

hand_bid = {}

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []

LABEL_VALUE = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1
}

pointer_mapper = {
    "five_kind": five_kind,
    "four_kind": four_kind,
    "full_house": full_house,
    "three_kind": three_kind,
    "two_pair": two_pair,
    "one_pair": one_pair,
    "high_card": high_card
}

def get_type(hand):
    m = {}
    for c in hand:
        if c not in m:
            m[c] = 0
        m[c] += 1

    if len(m) == 5:
        return "high_card"
    if len(m) == 4:
        return "one_pair"
    if len(m) == 1:
        return "five_kind"
    if len(m) == 3:
        for k in m:
            if m[k] == 3:
                return "three_kind"
            
        return "two_pair"
    
    for k in m:
        if m[k] == 4:
            return "four_kind"
        
    return "full_house"

def compare(hand1, hand2):
    for i in range(5):
        if LABEL_VALUE[hand1[i]] > LABEL_VALUE[hand2[i]]:
            return 1
        if LABEL_VALUE[hand1[i]] < LABEL_VALUE[hand2[i]]:
            return -1
        
    return 0

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    first_half = merge_sort(arr[:len(arr) // 2])
    second_half = merge_sort(arr[len(arr) // 2:])
    res = []
    while first_half or second_half:
        if not first_half:
            res.extend(second_half)
            break

        if not second_half:
            res.extend(first_half)
            break

        if compare(first_half[0],second_half[0]) == 0 or compare(first_half[0],second_half[0]) == 1:
            item = first_half.pop(0)
            res.append(item)
        else:
            item = second_half.pop(0)
            res.append(item)
        
    return res

for line in data:
    hand, bid = line.split(" ")
    hand_bid[hand] = int(bid)

total_hand = len(hand_bid)

for k in hand_bid:
    hand_type = get_type(k)
    pointer = pointer_mapper[hand_type]
    pointer.append(k)

pipeline = [five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card]

current_multipler = total_hand

res = 0

for kind in pipeline:
    sorted_hand = merge_sort(kind)
    for hand in sorted_hand:
        res += (hand_bid[hand] * current_multipler)
        current_multipler -= 1

print(res)
