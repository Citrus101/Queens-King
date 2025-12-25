def board_valid(board:list, n:int) -> bool:
    ...
    
def check_row(board:list, n:int, row:int) -> bool:
    ...

def check_col(board:list, n:int, col:int) -> bool:
    ...

def check_surrounding(board:list, n:int, row:int, col:int) -> bool:
    ...

    
def board_valid(board:list, n:int) -> bool:

    for i in range(n):
        sum = 0;
        sum += check_row(board, n, i);
        print("check row", sum);
        if(sum != 1): return False;
        sum = 0;
        sum += check_col(board, n, i);
        print("check col", sum);
        if(sum != 1): return False;
        
    return True;
        

def check_row(board:list, n:int, row:int) -> bool:
    sum = 0;
    for i in range(n):
        idx = row * n + i;
        sum += board[idx];
        if(board[idx] == 1):
            sum += check_surrounding(board, n, row, i);
    
    return (sum == 1);

def check_col(board:list, n:int, col:int) -> bool:
    sum = 0;
    for i in range(n):
        idx = (i * n) + col;
        sum += board[idx];
        if(board[idx] == 1):
            sum += check_surrounding(board, n, i, col);
    
    return (sum == 1);

def check_surrounding(board:list, n:int, row:int, col:int) -> bool:

    idx = (row - 1) * n + col      #N

    if((row - 1) >= 0 and board[idx]): return True;

    idx = (row - 1) * n + col + 1  #NE
    if((row - 1) >= 0 and col < n and board[idx]): return True;

    idx = (row) * n + col + 1      #E
    if(col < n and board[idx]): return True;
    
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

# print(board_valid(nice, 5));