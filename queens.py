from collections import defaultdict
import gc
import time
import cProfile
import pstats        
import pyautogui
from pynput import mouse
from pynput.mouse import Controller, Button

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

mouse_controller = Controller()

# -------------------------------
# Wait for a mouse click
# -------------------------------
def get_mouse_click_position():
    print("Click anywhere on the screen...")

    position = {"x": None, "y": None}

    def on_click(x, y, button, pressed):
        if pressed:
            position["x"] = x
            position["y"] = y
            print(f"Clicked at ({x}, {y})")
            return False  # Stop listener

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    return position["x"], position["y"]

def click_at(x, y, button=Button.left):
    mouse_controller.position = (x, y)
    mouse_controller.click(button, 2)
# -------------------------------
# Take screenshot
# -------------------------------
def take_screenshot():
    return pyautogui.screenshot()

def iterate_from_point(image, start_x, start_y):
    global n
    global first_block_x
    global first_block_y
    global block_s
    
    width, height = image.size
    boundary = []
    filename = "pixels1.txt"
    pixels = image.load()
    prev_colour = 0;
    curr_colour = 0;
    for x in range(start_x , start_x + 1):
        for y in range(start_y, height):
            curr_colour = pixels[x, y];
            if(curr_colour == (0, 0, 0) and curr_colour != prev_colour):
                boundary.append([x, y])
            prev_colour = curr_colour

    n = len(boundary) - 1
    block_s = (boundary[1][1] - boundary[0][1])
    d = {}
    count = 1;
    first_block_x = start_x;
    first_block_y = boundary[1][1] - block_s / 2;


    for i in range(1, n + 1):
        y = boundary[i][1] - block_s / 2;
        for j in range(n):
            x = start_x + block_s * (95 * j) / 100;
            print(pixels[x, y], end = " ")
            # click_at(x, y)
            if(not (pixels[x, y] in d)):
                d[pixels[x, y]] = count;
                count += 1
            nice.append(d[pixels[x, y]]);
        

nice = []


inc_perm_state = 0
def inc_perm(key:int, inside_loop:bool):
    
    global curr
    global kill_switch
    global inc_perm_state

    lcurr = key
    if((inside_loop) and (idx_array[lcurr] == ((len_colours[lcurr]) - 1))):
        return;
    if(inside_loop):
        inc_perm_state = 1;
    else: 
        if(inc_perm_state):
            inc_perm_state = 0
            return;

    idx_array[key] += 1

    while(idx_array[lcurr] >= len_colours[lcurr]):


        idx_array[lcurr] = 0
        lcurr -= 1
        idx_array[lcurr] += 1
        if(idx_array[1] >= len_colours[1]): kill_switch = True
        if(lcurr == 0): break;

    curr = n 


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

n = 9

coords_dict = defaultdict(list)
len_colours = []
idx_array = [0] * (9 + 1)
curr = n
kill_switch = False;
board_coords = []
count = 0
first_block_x = 0;
first_block_y = 0;
block_s = 0;

def main():    
    global count
    global nice 
    global n
    global len_colours
    global coords_dict
    
    x, y = get_mouse_click_position()
    img = take_screenshot()
    iterate_from_point(img, 720, 250)
    
    for i in range(0, n * n):
        coords_dict[nice[i]].append(i)

    len_colours = [0] + [len(coords_dict[i]) for i in coords_dict]
        
    with open("board", "w") as f:
        ...
        
    options = [];
    start = time.time()
    while(1):
        row  = [0] * (n + 1)
        col  = [0] * (n + 1)
        display_board = True;
        for key in coords_dict:

            idx = coords_dict[key][idx_array[key]]
            r = int(idx / n);
            c = idx % n;

            if((row[r]) or col[c]): 
                display_board = False;
                inc_perm(key, True)
                idx = coords_dict[key][idx_array[key]]
                break;
            
            row[r] = 1;
            col[c] = 1;
        
        if(display_board):
            what = [0] * (n * n)
            for key in coords_dict:
                idx = coords_dict[key][idx_array[key]];
                what[idx] = 1;
            options.append(what)
            count += 1;
        inc_perm(n, False);


    
        if(kill_switch == True): break;

    nice = 0
    for _ in options:
        row = [0] * (n);
        col = [0] * (n);
        for i in range(n * n):
            if(_[i] == 0): continue;
            r = int(i / n);
            c = i % n;
            if(check_surrounding(_, n, r, c)): break;

            row[r] = 1;
            col[c] = 1;
        else:
            for i in range(n):
                for j in range(n):
                    if(_[i*n + j] == 1):
                        
                        x = first_block_x + j * (95 * block_s) / 100; 
                        y = first_block_y + i * (95 * block_s) / 100;
                        click_at(x, y)
                    print(_[i * n + j], end=" ");
                print() 
            break;
            

    end = time.time()
    print(end - start)
    print(count)
    print(nice)

if __name__ == "__main__":
    gc.disable()
    cProfile.run("main()", "profile.stats")
    p = pstats.Stats("profile.stats")
    p.strip_dirs().sort_stats("cumtime").print_stats(20)