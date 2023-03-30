from math import sqrt
import time


class Node:
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

    f = open("input3.txt", "r")
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
    for row in maze:
        for col in row:
            if col == "-":
                print('\x1b[0;31;40m' + str(col) + '\x1b[0m', end=" ")
            elif col == "+":
                print('\x1b[0;30;41m' + str(col) + '\x1b[0m', end=" ")
            else:
                print(str(col), end=" ")
        print()


def a_star(maze):
    path = []
    # initialize open and closed list. Open list stores nodes that still can be visited,
    # closed list stores visited nodes
    open_list = []
    closed_list = []

    # find the x and y coordinates of starting symbol 's' and finishing symbol 'e'
    row, col = find_ids(maze, 's')
    row_f, col_f = find_ids(maze, 'e')

    # create starting node, set its parameters to x and y coordinates of starting symbol, and g, h and f to 0.
    # As it is the first node, it has no parent. Append the node to the open_list
    start_node = Node(None, row, col)
    start_node.g = 0
    start_node.h = 0
    start_node.f = 0

    open_list.append(start_node)

    iteration = 0
    while len(open_list) != 0:
        print("Iteration " + str(iteration))

        # Find node with smallest value of f to be the current node
        curr_node = open_list[0]
        for item in open_list:
            if item.f < curr_node.f:
                curr_node = item

        # Move the node from open_list to closed_list
        open_list.remove(curr_node)
        closed_list.append(curr_node)

        # Check if the current node is the exit (finish). If so, we are backtracking the shortest path looking
        # at parents of the nodes, starting from the current node (the finish)
        if curr_node.x == row_f and curr_node.y == col_f:
            print("You've found the exit")
            curr = curr_node
            while curr is not None:
                path.append([curr.x, curr.y])
                curr = curr.parent
            break

        # Generate four children of the current node
        children = [[curr_node.x + 1, curr_node.y], [curr_node.x, curr_node.y + 1],
                    [curr_node.x - 1, curr_node.y], [curr_node.x, curr_node.y - 1]]
        print(children)

        for child in children:
            print("Current node")
            print(child[0:2])

            # For each child check, if it is not a wall
            if maze[child[0]][child[1]] != "#":

                child_node = Node(curr_node, child[0], child[1])
                # Check if the child is not in the closed list, that is, if it was not visited yet.
                # If so, then continue to the next child
                if closed_list.__contains__(child_node):
                    print("Closed list contains node")
                    continue

                # Asses the child's parameters: g being the distance from the starting node,
                # h, that is the distance from the finishing node and f, which is the sum of previous ones
                child_node.g = curr_node.g + 1
                child_node.h = h_euclidean(child_node.x, child_node.y, row_f, col_f)
                child_node.f = child_node.g + child_node.h

                # Lastly check if the node is not already present in the open_list. If it is we have to compare
                # its g parameter, the distance traversed from the starting node. If it is higher, than we continue to
                # the next child. If it is not on the list, then we add the node to the open_list
                if open_list.__contains__(child_node):
                    for open_node in open_list:
                        if child_node == open_node:
                            if child_node.g >= open_node.g:
                                print("G value of new node is higher than the its value from the open list")
                                break
                            else:
                                open_list.remove(child_node)
                                open_list.append(child_node)
                                break
                else:
                    print("Append")
                    print(str(child_node.g))
                    open_list.append(child_node)

            else:
                print("Wall")
        print()
        iteration = iteration + 1
        if maze[curr_node.x][curr_node.y] != 's' and maze[curr_node.x][curr_node.y] != 'e':
            maze[curr_node.x][curr_node.y] = '-'
        print_maze(maze)
        # time.sleep(0.2)

    print(path)
    for i in path:
        if maze[i[0]][i[1]] != 's' and maze[i[0]][i[1]] != 'e':
            maze[i[0]][i[1]] = '+'


maze = read_file()
print_maze(maze)
a_star(maze)
print_maze(maze)
