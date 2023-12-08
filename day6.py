data = open('day6.txt', 'r').read().split('\n')
line_time = data[0]
line_distance = data[1]
distance_arr = line_distance.split(" ")
time_arr = line_time.split(" ")
time = []
distance = []
for item in time_arr[1:]:
    if item != "":
        time.append(int(item))

for item in distance_arr[1:]:
    if item != "":
        distance.append(int(item))


def solve(distance, time):
    res = 0
    for i in range(1,time+1):
        if distance <= (time - i) * i:
            res += 1

    return res

total = 1

for i in range(len(time)):
    total *= solve(distance[i], time[i])

print(total)