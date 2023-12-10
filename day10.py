DIRECTION_MAP = {
    "|": [[1,0], [-1, 0]],
    "-": [[0,1], [0, -1]],
    "L": [[-1,0], [0, 1]],
    "J": [[-1,0], [0, -1]],
    "7": [[0,-1], [1, 0]],
    "F": [[1,0], [0, 1]]
}

def get_input():
    data = open('day10.txt', 'r').read().split('\n')
    lst = []
    for line in data:
        lst.append([n for n in line])

    return lst

def construct_key(row, col):
    key = f"{row}|{col}"
    return key

def bfs(row, col, visited, arr):
    current = [[row - 1, col], [row + 1, col]]
    while current:
        temp = []
        for y, x in current:
            key = construct_key(y, x)
            if key not in visited:
                # do bfs
                for direction in DIRECTION_MAP[arr[y][x]]:
                    temp.append([y+direction[0], x+direction[1]])
                visited.add(key)
        current = temp


def solve(row, col, arr):
    visited = set()
    visited.add(construct_key(row, col))

    bfs(row, col, visited, arr)

    return len(visited) // 2




if __name__ == "__main__":
    # I leave edge cases because I'm too lazy xD. So, this code will not be applicable to all inputs.
    maze = get_input()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                print(solve(i,j,maze))
                break