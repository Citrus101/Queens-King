from collections import defaultdict
# import board_check
import time

def inc_perm():
    ...

def check_row(board:list, n:int, row:int) -> bool:
    sum = 0;
    for i in range(n):
        idx = row * n + i;
        sum += board[idx];
        # if(board[idx] == 1):
            # sum += check_surrounding(board, n, row, i);
    
    return (sum == 1);

def print_board(board:list, n:int):
    filename = "board"
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # print(board)
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # print("===============================================================")
    append_list_to_file(filename, board);
    # for i in range(n):
    #     for j in range(n):
    #         print(what[i * n + j], end=" ")
    #     print()
    # print("===============================================================")

def append_list_to_file(filename: str, items: list) -> None:

    with open(filename, "a") as f:
        f.write("===============================================================\n")
        for i in range(n):
            for j in range(n):
                f.write(f"{what[i * n + j]} ")
            f.write("\n")
        f.write("===============================================================\n")


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
n = 3

coords_dict = defaultdict(list)
# color_coords[2] = 3;

for i in range(1, n + 1):
    # coords_dict[nice[i]].append(i)
    for j in range(n):
        coords_dict[i].append(n * (i - 1) + j)


idx_array = [0] * (n + 1)
curr = n
kill_switch = False;
count = 0
# idx = 0

start = time.time()
nice = 0;
with open("board", "w") as f:
    ...

def inc_perm():
    
    global curr
    global kill_switch
    idx_array[curr] += 1

    while(idx_array[curr] >= len(coords_dict[curr])):

        # print(idx_array[curr], end=" ")
        # print(len(coords_dict[curr]))
        # print(curr);

        idx_array[curr] = 0
        curr -= 1
        idx_array[curr] += 1
        if(idx_array[1] >= len(coords_dict[1])): kill_switch = True
        if(curr == 0): break;

    curr = n 

while(1):
    what = [0] * (n * n)
    row  = [0] * (n + 1)
    col  = [0] * (n + 1)
    # s = time.time();
    for key in coords_dict:
        idx = coords_dict[key][idx_array[key]]

        r = int(idx / n);
        c = idx % n;

        while(row[r] or col[c]):
            print_board(what, n);
            inc_perm();
            idx = coords_dict[key][idx_array[key]]

            r = int(idx / n);
            c = idx % n;

        what[idx] = 1
        row[r] = 1;
        col[c] = 1;
        # what[coords_dict[key][idx_array[key]]] = 1
        # row[]
        # if(check_row(what, n, idx)): continue
    inc_perm();

    # print_board(what, n)
    # e = time.time();
    # nice += e - s;

   
    count += 1;
    if(kill_switch == True): break;

    # print(what)

end = time.time()
print(end - start)
# print(nice)
print(count)
