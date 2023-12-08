data = open('day3.txt', 'r').read().split('\n')

def find_digit(row, col, arr):
    '''
    [1,1,1]
    [1,1,1]
    [0,1,1]
    '''
    if row - 1 >= 0:
        if not arr[row - 1][col].isdigit() and arr[row - 1][col] != ".":
            return True
        if col - 1 >= 0:
            if not arr[row - 1][col - 1].isdigit() and arr[row - 1][col - 1] != ".":
                return True
        if col + 1 < len(arr[row - 1]):
            if not arr[row - 1][col + 1].isdigit() and arr[row - 1][col + 1] != ".":
                return True
    if col - 1 >= 0:
        if not arr[row][col - 1].isdigit() and arr[row][col - 1] != ".":
            return True
    
    if col + 1 < len(arr[row]):
        if not arr[row][col + 1].isdigit() and arr[row][col + 1] != ".":
            return True
        
    if row + 1 < len(arr):
        if not arr[row + 1][col].isdigit() and arr[row + 1][col] != ".":
            return True
        if col + 1 < len(arr[row + 1]):
            if not arr[row + 1][col + 1].isdigit() and arr[row + 1][col + 1] != ".":
                return True
        if col - 1 >= 0:
            if not arr[row + 1][col - 1].isdigit() and arr[row + 1][col - 1] != ".":
                return True

        
    return False


res = 0

for i in range(len(data)):
    line = data[i]
    for j in range(len(line)):
        element = line[j]
        if element.isdigit(): # need to check is it valid or not
            if j == 0 or not line[j - 1].isdigit(): #first of the line / first digit / begin character of number
                current_number = ""
                isValid = False
                for k in range(j,len(line)):
                    if not line[k].isdigit():
                        break
                    current_number += line[k]
                    isValid = isValid or find_digit(i, k, data)

                if isValid:
                    res += int(current_number)

print(res)