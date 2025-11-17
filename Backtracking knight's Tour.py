N = 8

# Chessboard
board = [[-1]*N for _ in range(N)]

# Knight moves
moves = [(2,1),(1,2),(-1,2),(-2,1),
         (-2,-1),(-1,-2),(1,-2),(2,-1)]

def safe(x, y):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def solve(x, y, step):
    if step == N*N:
        return True

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if safe(nx, ny):
            board[nx][ny] = step
            if solve(nx, ny, step + 1):
                return True
            board[nx][ny] = -1
    return False

# Start at (0,0)
board[0][0] = 0

if solve(0, 0, 1):
    for r in board:
        print(r)
else:
    print("No Tour Found")
