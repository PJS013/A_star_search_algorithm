from math import sqrt


def h_manhattan(current_cell_x, current_cell_y, goal_x, goal_y):
    return abs(current_cell_x - goal_x) + abs(current_cell_y - goal_y)


def h_euclidean(current_cell_x, current_cell_y, goal_x, goal_y):
    return sqrt(pow(current_cell_x - goal_x, 2) + pow(current_cell_y - goal_y, 2))


def read_file(file):
    maze = []

    f = open(file, "r")
    for line in f.readlines():
        maze.append([x.strip('\n') for x in line if x != '\n'])
    return maze


# Helper function returning the position of character in the array
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
    for row in maze:
        for col in row:
            print(str(col), end=" ")
        print()
