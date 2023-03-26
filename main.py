from math import sqrt


def h_manhattan(current_cell_x, current_cell_y, goal_x, goal_y):
    return abs(current_cell_x - goal_x) + abs(current_cell_y - goal_y)


def h_euclidean(current_cell_x, current_cell_y, goal_x, goal_y):
    return sqrt(pow(current_cell_x - goal_x, 2) + pow(current_cell_y - goal_y, 2))


def read_file():
    maze = []

    f = open("input2.txt", "r")
    for line in f.readlines():
        maze.append([x.strip('\n') for x in line if x != '\n'])
    return maze


def find_ids(maze, char):
    y = 0
    for row in maze:
        x = 0
        for col in row:
            if col == char:
                return y, x
            x += 1
        y += 1


def find_id_of_col_with_min_val(arr):
    min_val = arr[0][2]
    min_col_index = 0
    if len(arr)>1:
        for i in range(1, len(arr)):
            if arr[i][2] < min_val:
                min_val = arr[i][2]
                min_col_index = i

    # Print the index of the column with the minimum value in the 3rd row
    print("Column index with minimum value in 3rd row:", min_col_index)
    return min_col_index


def does_it_contain(closed_list, curr_node):
    for node in closed_list:
        if node[0:2] == curr_node[0:2]:
            return 1


def open_list_node_higher_or_lower(open_list, curr_node):
    for node in open_list:
        if node[0:2] == curr_node[0:2]:
            if curr_node[2] > node[2]:
                return 1
            else:
                return 0


def print_maze(maze):
    for x in maze:
        for i in x:
            if i == "-":
                print('\x1b[0;31;40m' + str(i) + '\x1b[0m', end=" ")
            else:
                print(str(i), end=" ")
        print()


maze = []
maze = read_file()
for i in maze:
    print(i)

open_list = []
closed_list = []
print()
row, col = find_ids(maze, 's')
row_f, col_f = find_ids(maze, 'e')
open_list.append([row,col,0])
# open_list.append([1,1,1])
# open_list.append([2,2,2])
# open_list.append([3,3,3])
# open_list.append([4,4,4])
# open_list.append([5,5,5])
print(open_list)
g = 1
flag = 'n'
while len(open_list)!=0:
    print("Iteration " + str(g))
    id = find_id_of_col_with_min_val(open_list)
    curr_node = open_list[id]
    print("curr_node")
    print(curr_node)
    open_list.remove(curr_node)
    # print("after removal")
    # print(curr_node)
    # print(open_list)
    closed_list.append(curr_node)
    if curr_node[0] == row_f and curr_node[1] == col_f:
        print("You've found the exit")
        flag = 'e'
        break
    children = [[curr_node[0]+1, curr_node[1], 100000000],[curr_node[0],curr_node[1]+1, 100000000],[curr_node[0]-1,curr_node[1], 100000000],[curr_node[0],curr_node[1]-1, 100000000]]
    print(children)
    for node in children:
        print("Current node")
        print(node)
        if maze[node[0]][node[1]] != "#":
            # print("Abc")
            if does_it_contain(closed_list, node) == 1:
                print("Closed list contains node")
                continue
            # print("Easy")
            if node[0] == row_f and node[1] == col_f:
                flag = 'e'
                print("The exit is found")
                break
            # print("As")
            node[2] = g + h_manhattan(node[0], node[1], row_f, col_f)
            if open_list_node_higher_or_lower(open_list, node) == 1:
                continue
            print("Append")
            print(node)
            open_list.append(node)
    print("open list after")
    print(open_list)
    print("Closed list after")
    print(closed_list)
    print()
    g = g + 1
    if flag == 'e':
        break
    # input()
for node in closed_list:
    maze[node[0]][node[1]] = '-'

print_maze(maze)
