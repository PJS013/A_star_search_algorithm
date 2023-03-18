def read_file():
    maze = []

    f = open("input.txt", "r")
    for line in f.readlines():
        maze.append([x.strip('\n') for x in line if x != '\n'])
    return maze


maze = []
maze = read_file()
for i in maze:
    print(i)

open_list = []
closed_list = []