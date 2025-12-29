from collections import defaultdict
import gc
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
    
    return (sum == 1);

def print_board(board:list, n:int):
    filename = "board"
    # print(what)
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
                f.write(f"{items[i * n + j]} ")
            f.write("\n")
        f.write("===============================================================\n")

def display_board__():
    what = [0] * (n * n);
    for key in coords_dict:
        idx = coords_dict[key][idx_array[key]];
        what[idx] = 1;

    print("===============================================================")
    for i in range(n):
        for j in range(n):
            # idx = coords_dict[key][idx_array[key]]
            print(what[i * n + j], end=" ")
        print()

    print("===============================================================")


# nice = [
#     1, 1, 1, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 2, 2, 2, 2, 3, 1,
#     1, 1, 2, 2, 4, 5, 2, 3, 1,
#     1, 6, 4, 4, 4, 4, 3, 3, 1,
#     1, 6, 6, 4, 7, 7, 3, 3, 1,
#     1, 6, 6, 4, 7, 7, 3, 1, 1,
#     8, 6, 6, 4, 7, 7, 1, 1, 1,
#     8, 8, 9, 9, 9, 9, 1, 1, 1,
#     8, 8, 8, 9, 9, 9, 9, 1, 1,
# ]

nice = [
    1, 2, 2, 2, 2, 2, 2, 2, 3,
    1, 4, 4, 1, 2, 3, 5, 5, 3,
    1, 1, 4, 1, 2, 3, 5, 3, 3,
    6, 1, 1, 1, 2, 3, 3, 3, 6,
    6, 6, 7, 7, 2, 6, 6, 6, 6,
    6, 6, 6, 2, 2, 2, 6, 1, 6,
    6, 8, 6, 6, 6, 6, 6, 8, 6,
    6, 8, 8, 8, 8, 8, 8, 8, 9,
    6, 6, 8, 8, 8, 8, 8, 9, 9,
]

# nice = [
#     1, 1, 2, 2, 2, 3, 3, 4,
#     1, 2, 2, 2, 3, 3, 4, 4,
#     2, 2, 2, 3, 3, 5, 4, 6,
#     2, 2, 3, 3, 5, 5, 6, 6,
#     2, 3, 3, 5, 5, 6, 6, 7,
#     3, 3, 3, 5, 5, 5, 8, 7,
#     3, 3, 3, 5, 5, 8, 8, 7,
#     5, 5, 5, 5, 8, 8, 7, 7,

# ]

# nice = [
#     1, 1, 1, 1, 1, 1, 1, 2,
#     1, 3, 3, 2, 4, 4, 2, 2,
#     1, 3, 3, 2, 4, 4, 2, 2,
#     1, 1, 1, 5, 2, 2, 2, 2,
#     1, 6, 6, 7, 8, 8, 2, 2,
#     6, 6, 7, 7, 7, 8, 8, 2,
#     6, 2, 2, 2, 2, 2, 8, 2,
#     2, 2, 2, 2, 2, 2, 2, 2,

# ]

# nice = [
#     1, 1, 1, 1, 1, 1, 1, 2,
#     1, 3, 3, 2, 4, 4, 2, 2,
#     1, 3, 3, 2, 4, 4, 2, 2,
#     1, 1, 1, 5, 2, 2, 2, 2,
#     1, 6, 6, 7, 8, 8, 2, 2,
#     6, 6, 7, 7, 7, 8, 8, 2,
#     6, 2, 2, 2, 2, 2, 8, 2,
#     2, 2, 2, 2, 2, 2, 2, 2,

# ]
n = 9

coords_dict = defaultdict(list)
# color_coords[2] = 3;

for i in range(0, n*n ):
# for i in range(1, n + 1):
    coords_dict[nice[i]].append(i)
    # for j in range(n):
    #     coords_dict[i].append(n * (i - 1) + j)
print(coords_dict)

len_colours = [0] + [len(coords_dict[i]) for i in coords_dict]
print(len_colours)
idx_array = [0] * (n + 1)
curr = n
kill_switch = False;
board_coords = []
count = 0
nice = 0
# idx = 0

inc_perm_state = 0
def inc_perm(key:int, inside_loop:bool):
    
    global curr
    global kill_switch
    global inc_perm_state

    lcurr = key
    # lcurr = key
    # print(not inside_loop)
    if((inside_loop) and (idx_array[lcurr] == ((len_colours[lcurr]) - 1))):
        return;
    if(inside_loop):
        inc_perm_state = 1;
    else: 
        if(inc_perm_state):
            inc_perm_state = 0
            return;

    idx_array[key] += 1
    # break_loop = False;

    while(idx_array[lcurr] >= len_colours[lcurr]):

        # print(idx_array[curr], end=" ")
        # print(len(coords_dict[curr]))
        # print(curr);

        idx_array[lcurr] = 0
        lcurr -= 1
        idx_array[lcurr] += 1
        # print(f"nice: {idx_array[1]} whatwhat: {len(coords_dict[1])}");
        if(idx_array[1] >= len_colours[1]): kill_switch = True
        # print(kill_switch)
        if(lcurr == 0): break;

    curr = n 

# def check_surrounding(row:int, col:int, row_list:list, col_list:list) -> bool:

#     #N
#     print("north")
#     if((row - 1) >= 0 and row_list[row - 1] and col_list[col]): return True; 

#     #NE
#     print("north east")
#     if((row - 1) >= 0 and (col + 1) < n and row_list[row - 1] and col_list[col + 1]): return True;

#     #E
#     print("east")
#     if((col + 1) < n and row_list[row] and col_list[col + 1]): return True;
    
#     #SE
#     print("south east")
#     if((row + 1) < n and (col + 1) < n and row_list[row + 1] and col_list[col + 1]): return True;
    
#     #S
#     print("south")
#     if((row + 1) < n and row_list[row + 1] and col_list[col]): return True;
    
#     #SW
#     print("south west")
#     if((row + 1) < n and (col - 1) >= 0 and row_list[row + 1] and col_list[col - 1]): return True;
    
#     #W
#     print("west")
#     if((col - 1) >= 0 and row_list[row] and col_list[col - 1]): return True;
    
#     #NW
#     print("north west")
#     if((row + 1) < n and (col - 1) >= 0 and row_list[row + 1] and col_list[col - 1]): return True;
#     return False;

def check_surrounding(board:list, n:int, row:int, col:int) -> bool:

    idx = (row - 1) * n + col      #N

    if((row - 1) >= 0 and board[idx]): return True;

    idx = (row - 1) * n + col + 1  #NE
    if((row - 1) >= 0 and col < n and board[idx]): return True;

    idx = (row) * n + col + 1      #E
    if((col + 1) < n and board[idx]): return True;
    
    idx = (row + 1) * n + col + 1  #SE
    if((row + 1) < n and (col + 1) < n and board[idx]): return True;
    
    idx = (row + 1) * n + col      #S
    if((row + 1) < n and board[idx]): return True;
    
    idx = (row - 1) * n + col - 1  #SW
    if((row - 1) >= 0 and (col - 1) >= 0 and board[idx]): return True;
    
    idx = (row) * n + col - 1      #W
    if((col - 1) >= 0 and board[idx]): return True;
    
    idx = (row - 1) * n + col - 1  #NW
    if((row - 1) >= 0 and (col - 1) >= 0 and board[idx]): return True;

    return False;
def main():    
    global count
    global nice 
    with open("board", "w") as f:
        ...
        
    options = [];
    start = time.time()
    while(1):
        # board_coords;
        # row  = 0
        # col  = 0
        row  = [0] * (n + 1)
        col  = [0] * (n + 1)
        display_board = True;
        # update_board = True;
        # s = time.time();
        for key in coords_dict:

            idx = coords_dict[key][idx_array[key]]
            r = int(idx / n);
            c = idx % n;

            # if((row & (1 << r)) or (col & (1 << c))): 
            # print("PRE")
            # if((row[r]) or col[c] or check_surrounding(r, c, row, col)): 
            if((row[r]) or col[c]): 
                # display_board__()
                display_board = False;
                # print("BROKEN")
                inc_perm(key, True)
                # print([key])
                # print(idx_array)
                # print(coords_dict[key])
                # print(len_colours)
                # print(coords_dict)
                idx = coords_dict[key][idx_array[key]]
                # r = int(idx / n);
                # c = idx % n;
                break;
            # print("NICE")
            
                
            # while(((row[r]) or (col[c])) or not update_board): 

            #     display_board = False;
            #     idx = coords_dict[key][idx_array[key]]
            #     r = int(idx / n);
            #     c = idx % n;
            #     update_board = inc_perm()
            # row |= (1 << r);
            # col |= (1 << c);
            row[r] = 1;
            col[c] = 1;
        
        # e = time.time();
        # nice += e - s;
        # def board_check():
        if(display_board):
            # display_board__()
            what = [0] * (n * n)
            for key in coords_dict:
                idx = coords_dict[key][idx_array[key]];
                what[idx] = 1;
            # print(what)
            options.append(what)
            # print_board(what, n)
            count += 1;
        # board_check()
        inc_perm(n, False);


    
        if(kill_switch == True): break;

    # print(what)
    # print("STARTINF FILTER")
    nice = 0
    for _ in options:
        row = [0] * (n);
        col = [0] * (n);
        # print(_)
        for i in range(n * n):
            if(_[i] == 0): continue;
            # print("reached")
            r = int(i / n);
            c = i % n;
            if(check_surrounding(_, n, r, c)): break;

            row[r] = 1;
            col[c] = 1;
            # print(f"row: {row}, col: {col}")
        else:
            # print("enter ")
            for i in range(n):
                for j in range(n):
                    print(_[i * n + j], end=" ");
                print()
            break;
            
    # print("ENDING FILTER")

                

    end = time.time()
    print(end - start)
    print(count)
    print(nice)

if __name__ == "__main__":
    gc.disable()
    cProfile.run("main()", "profile.stats")
    p = pstats.Stats("profile.stats")
    p.strip_dirs().sort_stats("cumtime").print_stats(20)