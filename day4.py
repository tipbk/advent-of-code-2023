data = open('day4.txt', 'r').read().split('\n')

def solve(arr1, arr2):
    s = set()
    for element in arr1:
        s.add(element)

    total = 0
    for element in arr2:
        if element in s:
            total += 1


    if total == 0:
        return 0
    
    return 2 ** (total - 1)

res = 0

# refine data
for line in data:
    numbers = line.split(": ")[1]
    arr = numbers.split(" | ")
    winning_number = arr[0]
    new_winning_number = winning_number.split(" ")
    winning_number_refined = []
    for item in new_winning_number:
        if item.strip() != "":
            winning_number_refined.append(item)

    our_number = arr[1]
    new_our_number = our_number.split(" ")
    our_number_refined = []
    for item in new_our_number:
        if item.strip() != "":
            our_number_refined.append(item)
    
    res += solve(winning_number_refined, our_number_refined)

print(res)