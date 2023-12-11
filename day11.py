def get_input():
    data = open('day11.txt', 'r').read().split('\n')
    lst = []
    for line in data:
        lst.append([n for n in line])

    return lst

def solve(space):
    m = {}
    # space expanding on row
    row_expanded_space = []
    for i in range(len(space)):
        temp = []
        double = True
        for j in range(len(space[i])):
            if j not in m:
                m[j] = True
            temp.append(space[i][j])
            if space[i][j] == "#":
                double = False
                m[j] = False
        row_expanded_space.append(temp)
        if double:
            row_expanded_space.append(temp)

    # space expanding on col
    expanded_space = []
    for i in range(len(row_expanded_space)):
        temp = []
        for j in range(len(row_expanded_space[i])):
            if m[j]:
                temp.append(".")
            temp.append(row_expanded_space[i][j])
        expanded_space.append(temp)
            
    galaxies = []
    for i in range(len(expanded_space)):
        for j in range(len(expanded_space[i])):
            if expanded_space[i][j] == "#":
                galaxies.append([i,j])
    
    # O(n^2)
    res = 0
    for k in range(len(galaxies) - 1):
        y, x = galaxies[k]
        for l in range(k + 1, len(galaxies)):
            row, col = galaxies[l]
            res += abs(row - y) + abs(col - x)

    return res

if __name__ == "__main__":
    space = get_input()
    print(solve(space))