def read_file():
    maze = []

    f = open("input.txt", "r")
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
open_list.append([1,1,1])
open_list.append([2,2,2])
open_list.append([3,3,3])
open_list.append([4,4,4])
open_list.append([5,5,5])
print(open_list)
while len(open_list)!=0:
    id = find_id_of_col_with_min_val(open_list)
    curr_node = open_list[id]
    print(curr_node)
    open_list.remove(curr_node)
    print("after removal")
    print(curr_node)
    print(open_list)
    closed_list.append(curr_node)
    if curr_node[0] == row_f and curr_node[1] == col_f:
        print("You've found the exit")
        break
    children = []

