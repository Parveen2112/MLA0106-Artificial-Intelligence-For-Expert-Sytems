# checkers_minimax.py (simplified)
import math, random, copy

# board: 8x8, 'r' red pieces (AI), 'b' black pieces (human), '.' empty
def initial_board():
    b = [['.' for _ in range(8)] for _ in range(8)]
    for r in range(3):
        for c in range(8):
            if (r+c) % 2 == 1: b[r][c] = 'r'
    for r in range(5,8):
        for c in range(8):
            if (r+c) % 2 == 1: b[r][c] = 'b'
    return b

def print_board(b):
    print("  "+" ".join(map(str,range(8))))
    for i,row in enumerate(b):
        print(i, " ".join(row))
    print()

# Generate simple moves (forward diagonal, captures by jumping)
def moves_for(b, player):
    dirs = [(-1,-1),(-1,1)] if player=='b' else [(1,-1),(1,1)]
    opp = 'r' if player=='b' else 'b'
    res=[]
    for r in range(8):
        for c in range(8):
            if b[r][c]==player:
                for dr,dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<8 and 0<=nc<8 and b[nr][nc]=='.':
                        nb=copy.deepcopy(b); nb[nr][nc]=player; nb[r][c]='.'; res.append(nb)
                    # capture
                    jr, jc = r+2*dr, c+2*dc
                    if 0<=jr<8 and 0<=jc<8 and b[nr][nc]==opp and b[jr][jc]=='.':
                        nb=copy.deepcopy(b); nb[jr][jc]=player; nb[r][c]='.'; nb[nr][nc]='.'; res.append(nb)
    return res or [b]

def evaluate(b):
    rcount=sum(row.count('r') for row in b)
    bcount=sum(row.count('b') for row in b)
    return rcount - bcount  # AI wants higher

def terminal(b):
    return all(cell!='b' for row in b for cell in row) or all(cell!='r' for row in b for cell in row)

def minimax(b, depth, alpha, beta, maximizing):
    if depth==0 or terminal(b):
        return evaluate(b), b
    player = 'r' if maximizing else 'b'
    best=None
    if maximizing:
        val=-math.inf
        for nb in moves_for(b, player):
            v,_=minimax(nb, depth-1, alpha, beta, False)
            if v>val:
                val, best = v, nb
            alpha=max(alpha,val)
            if alpha>=beta: break
        return val,best
    else:
        val=math.inf
        for nb in moves_for(b, player):
            v,_=minimax(nb, depth-1, alpha, beta, True)
            if v<val:
                val, best = v, nb
            beta=min(beta,val)
            if beta<=alpha: break
        return val,best

# Play (Human vs AI)
def play():
    board=initial_board()
    turn='b'  # human starts
    print_board(board)
    while not terminal(board):
        if turn=='b':
            print("Your turn (enter from_row from_col to_row to_col) or 'm' for random move:")
            cmd=input().strip()
            if cmd=='m':
                board=random.choice(moves_for(board,'b'))
            else:
                try:
                    fr,fc,tr,tc=map(int,cmd.split())
                    if board[fr][fc]=='b' and board[tr][tc]=='.':
                        board[tr][tc]='b'; board[fr][fc]='.'
                    else:
                        print("Invalid, random move applied."); board=random.choice(moves_for(board,'b'))
                except:
                    print("Bad input, random move applied."); board=random.choice(moves_for(board,'b'))
            print_board(board); turn='r'
        else:
            print("AI thinking...")
            _, nb = minimax(board, 4, -math.inf, math.inf, True)
            board = nb
            print_board(board); turn='b'
    score=evaluate(board)
    print("Game over. Winner:", "AI (r)" if score>0 else "Human (b)" if score<0 else "Draw")

if __name__=='__main__': play()
