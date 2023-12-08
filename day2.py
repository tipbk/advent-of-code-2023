data = open('day2.txt', 'r').read().split('\n')

BENCHMARK = {
    "red": 12,
    "green": 13,
    "blue": 14
}

res = 0

for line in data:
    pre_section = line.split(": ")
    pre_section_arr = pre_section[0].split(" ")
    game_id = pre_section_arr[1]

    isViolated = False
    
    # set details
    sets = pre_section[1].split("; ")
    for s in sets:
        set_arr = s.split(", ")
        
        for item in set_arr:
            item_arr = item.split(" ")
            n = int(item_arr[0])
            color = item_arr[1]
            if n > BENCHMARK[color]:
                # violate
                isViolated = True

    if not isViolated:
        res += int(game_id)

print(res)

