data = open('day8.txt', 'r').read().split('\n')

WALKING_VALUE = {
    "L": 0,
    "R": 1
}

instruction = [c for c in data[0]]

m = {}

for line in data[3:]:
    key = line[:3]
    left = line[7:10]
    right = line[12:15]
    m[key] = [left, right]

current = "AAA"
res = 0
while True:
    if current == "ZZZ":
        break
    new_instruction = instruction.pop(0)
    current = m[current][WALKING_VALUE[new_instruction]]
    res += 1
    instruction.append(new_instruction)

print(res)
        