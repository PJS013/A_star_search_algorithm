def read_file():
    maze = []

    f = open("input.txt", "r")
    for line in f.readlines():
        maze.append([x.strip('\n') for x in line if x != '\n'])
    return maze

def find_ids(maze):
    y = 0
    for row in maze:
        x = 0
        for col in row:
            if col == 's':
                return y, x
            x += 1
        y += 1

maze = []
maze = read_file()
for i in maze:
    print(i)

open_list = []
closed_list = []
print()
row, col = find_ids(maze)
print(row)
print(col)
print(maze[row][col])
closed_list.append([row,col,0])
