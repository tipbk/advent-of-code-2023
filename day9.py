def get_input():
    data = open('day9.txt', 'r').read().split('\n')
    lst = []
    for line in data:
        lst.append([int(n) for n in line.split(" ")])

    return lst

def is_all_zeroes(input):
    for item in input:
        if item != 0:
            return False
    return True

def solve(input):
    current = []
    current.append(input.copy())
    is_not_all_zeroes = True
    while is_not_all_zeroes:
        arr = current[-1] # check last item in stack
        temp = []
        is_not_all_zeroes = False
        for i in range(1,len(arr)):
            temp.append(arr[i] - arr[i-1])

        is_not_all_zeroes = not is_all_zeroes(temp)
        current.append(temp)

    res = 0
    for item in current:
        res += item[-1]
            
    return res

if __name__ == "__main__":
    res = 0
    for element in get_input():
        res += solve(element)

    print(res)