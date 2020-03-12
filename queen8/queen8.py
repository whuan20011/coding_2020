def queen8(row, board):
    if row == 8:
        global res
        res += 1
        return
    for col in range(8):
        if can_put_queen(row, col, board):
            board[row][col] = 1
            queen8(row + 1, board)
            board[row][col] = 0
def can_put_queen(row, col, board):
    for i in range(row):
        if board[i][col] == 1:
            return False
    a = row
    b = col
    while a >= 0 and b >= 0:
        if board[a][b] == 0:
            a -= 1
            b -= 1
        else:
            return False
    c = row
    d = col
    while c >= 0 and d <= 7:
        if board[c][d] == 0:
            c -= 1
            d += 1
        else:
            return False
    return True
board = []
for _ in range(8):
    arr = []
    for _ in range(8):
        arr.append(0)
    board.append(arr)
res = 0
queen8(0, board)
print res
