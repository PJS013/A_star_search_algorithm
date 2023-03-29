from math import sqrt


class node():
    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.x = x
        self.y = y

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def h_manhattan(current_cell_x, current_cell_y, goal_x, goal_y):
    return abs(current_cell_x - goal_x) + abs(current_cell_y - goal_y)


def h_euclidean(current_cell_x, current_cell_y, goal_x, goal_y):
    return sqrt(pow(current_cell_x - goal_x, 2) + pow(current_cell_y - goal_y, 2))


def read_file():
    maze = []

    f = open("input123.txt", "r")
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


def print_maze(maze):
    for x in maze:
        for i in x:
            if i == "-":
                print('\x1b[0;31;40m' + str(i) + '\x1b[0m', end=" ")
            elif i == "+":
                print('\x1b[0;30;41m' + str(i) + '\x1b[0m', end=" ")
            else:
                print(str(i), end=" ")
        print()


maze = []
maze = read_file()
print_maze(maze)
path = []
open_list = []
closed_list = []
print()
row, col = find_ids(maze, 's')
row_f, col_f = find_ids(maze, 'e')

start_node = node(None, row, col)
start_node.g = 0
start_node.h = 0
start_node.f = 0
x = 0
open_list.append(start_node)
print(open_list)
flag = 'n'

while len(open_list) != 0:
    print("Iteration " + str(x))

    curr_node = open_list[0]
    for index, item in enumerate(open_list):
        if item.f < curr_node.f:
            curr_node = item

    open_list.remove(curr_node)
    closed_list.append(curr_node)
    if curr_node.x == row_f and curr_node.y == col_f:
        print("You've found the exit")
        flag = 'e'
        curr = curr_node
        while curr is not None:
            path.append([curr_node.x, curr_node.y])
            curr = curr.parent
        break

    children = [[curr_node.x + 1, curr_node.y, 100000000], [curr_node.x, curr_node.y + 1, 100000000],
                [curr_node.x - 1, curr_node.y, 100000000], [curr_node.x, curr_node.y - 1, 100000000]]
    print(children)
    for child in children:
        f2 = 'f'
        print("Current node")
        print(child)
        if maze[child[0]][child[1]] != "#":

            new_node = node(curr_node, child[0], child[1])

            for closed_node in closed_list:
                if closed_node == new_node:
                    print("Closed list contains node")
                    f2 = 't'
                    break

            if f2 == 't':
                continue

            if new_node.x == row_f and new_node.y == col_f:
                flag = 'e'
                print("The exit is found")
                curr = curr_node
                while curr is not None:
                    path.append([curr.x, curr.y])
                    curr = curr.parent
                break

            new_node.g = curr_node.g
            new_node.h = h_euclidean(child[0], child[1], row_f, col_f)
            new_node.f = new_node.g + new_node.f

            for open_node in open_list:
                if new_node == open_node and new_node.g > open_node.g:
                    print("node g higher")
                    continue

            print("Append")
            print(child)
            open_list.append(new_node)
    print("open list after")
    print(open_list)
    print("Closed list after")
    print(closed_list)
    print()
    x = x + 1
    if flag == 'e':
        break
    # input()
for node in closed_list:
    if maze[node.x][node.y] != 's':
        maze[node.x][node.y] = '-'

print(path)
for i in path:
    if maze[i[0]][i[1]] != 's':
        maze[i[0]][i[1]] = '+'

print_maze(maze)

