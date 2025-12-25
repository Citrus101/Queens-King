from collections import defaultdict
import board_check

def print_board(board:list, n:int):
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(board)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("===============================================================")
    for i in range(n):
        for j in range(n):
            print(what[i * n + j], end=" ")
        print()
    print("===============================================================")

nice = [
    1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 2, 2, 2, 2, 3, 1,
    1, 1, 2, 2, 5, 4, 2, 3, 1,
    1, 6, 5, 5, 5, 5, 3, 3, 1,
    1, 6, 6, 5, 7, 7, 3, 3, 1,
    1, 6, 6, 5, 7, 7, 3, 1, 1,
    8, 6, 6, 5, 7, 7, 1, 1, 1,
    8, 8, 9, 9, 9, 9, 1, 1, 1,
    8, 8, 8, 9, 9, 9, 9, 1, 1,
]
n = 9

coords_dict = defaultdict(list)
# color_coords[2] = 3;

for i in range(81):
    coords_dict[nice[i]].append(i)

n = 4
idx_array = [0] * (n + 1)
curr = n
coords_dict = {
    1 : [0, 1, 2, 3],
    2 : [4, 5, 6, 7],
    3 : [8, 9, 10, 11],
    4 : [12, 13, 14, 15],
}

kill_switch = False;
count = 0
while(1):
    what = [0] * (n * n)
    for key in coords_dict:
        what[coords_dict[key][idx_array[key]]] = 1

    print_board(what, n)


    idx_array[curr] += 1

    while(idx_array[curr] >= len(coords_dict[curr])):

        # print(idx_array[curr], end=" ")
        # print(len(coords_dict[curr]))
        # print(curr);

        idx_array[curr] = 0
        curr -= 1
        idx_array[curr] += 1
        if(idx_array[0] >= len(coords_dict[1])): kill_switch = True
        if(curr == 0): break;

    curr = n 
   
    count += 1;
    if(kill_switch == True): break;

    # print(what)


print(count)