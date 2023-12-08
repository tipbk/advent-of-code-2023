data = open('day1.txt', 'r').read().split('\n')

res = 0

for line in data:
    first_digit = ""
    last_digit = line[0]
    for c in line:
        if c.isdigit():
            if first_digit == "":
                first_digit = c
            last_digit = c
    string_number = f"{first_digit}{last_digit}"
    res += int(string_number)

print(res)
