from collections import defaultdict
# import board_check
import time
import cProfile
import pstats        

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
n = 7

coords_dict = defaultdict(list)
# color_coords[2] = 3;

for i in range(1, n + 1):
    # coords_dict[nice[i]].append(i)
    for j in range(n):
        coords_dict[i].append(n * (i - 1) + j)


len_colours = [0] + [len(coords_dict[i]) for i in coords_dict]

idx_array = [0] * (n + 1)
curr = n
kill_switch = False;
board_coords = []
count = 0
# idx = 0


def inc_perm():
    
    global curr
    global kill_switch
    idx_array[curr] += 1
    # break_loop = False;

    # if(idx_array[curr] == (len(coords_dict[curr]) - 1)); break_loop = True
    while(idx_array[curr] >= len_colours[curr]):

        # print(idx_array[curr], end=" ")
        # print(len(coords_dict[curr]))
        # print(curr);

        idx_array[curr] = 0
        curr -= 1
        idx_array[curr] += 1
        # print(f"nice: {idx_array[1]} whatwhat: {len(coords_dict[1])}");
        if(idx_array[1] >= len_colours[1]): kill_switch = True
        # print(kill_switch)
        if(curr == 0): break;

    curr = n 

    # return break_loop;


# def update_board(board_coords : list):

#     board = [0] * (n * n)
#     for key in board_coords:
#         board[key] = 1
    
#     return board
def main():    
    global count
    start = time.time()
    with open("board", "w") as f:
        ...
        
    while(1):
        # board_coords;
        row  = [0] * (n + 1)
        col  = [0] * (n + 1)
        display_board = True;
        # s = time.time();
        for key in coords_dict:

            idx = coords_dict[key][idx_array[key]]

            r = int(idx / n);
            c = idx % n;

            if(row[r] or col[c]): 
                display_board = False;
                break;
            row[r] = 1;
            col[c] = 1;

        if(display_board):
            what = [0] * (n * n)
            for key in coords_dict:
                idx = coords_dict[key][idx_array[key]];
                what[idx] = 1;
            count += 1;
            # print_board(what, n)

        inc_perm();

        # e = time.time();
        # nice += e - s;

    
        if(kill_switch == True): break;

    # print(what)

    # end = time.time()
    # print(end - start)
# # print(nice)
    print(count)
if __name__ == "__main__":
    cProfile.run("main()", "profile.stats")
    p = pstats.Stats("profile.stats")
    p.strip_dirs().sort_stats("cumtime").print_stats(20)