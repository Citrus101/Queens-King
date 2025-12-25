from collections import defaultdict
import board_check

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

idx_array = [0] * 4
curr = 3
coords_dict = {
    1 : [0, 1, 2],
    2 : [3, 4, 5],
    3 : [6, 7, 8],
}
kill_switch = False;
count = 0
while(1):
    what = [0] * 9
    for key in coords_dict:
        what[coords_dict[key][idx_array[key]]] = 1

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

    curr = 3 
    print("===============================================================")
    for i in range(3):
        for j in range(3):
            print(what[i * 3 + j], end=" ")
        print()
    print("===============================================================")
   
    count += 1;
    if(kill_switch == True): break;

    # print(what)


print(count)