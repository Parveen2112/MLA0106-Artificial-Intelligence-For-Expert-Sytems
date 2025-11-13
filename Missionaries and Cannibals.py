from collections import deque

def valid(m, c): 
    return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)

def next_states(s):
    m, c, b = s; mv=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    for mm, cc in mv:
        if b=='L': new=(m-mm,c-cc,'R')
        else: new=(m+mm,c+cc,'L')
        if 0<=new[0]<=3 and 0<=new[1]<=3 and valid(*new[:2]): yield new

def bfs():
    start, goal = (3,3,'L'), (0,0,'R')
    q = deque([(start,[start])])
    seen=set()
    while q:
        s,p=q.popleft()
        if s==goal: return p
        if s in seen: continue
        seen.add(s)
        for n in next_states(s): q.append((n,p+[n]))

for step in bfs(): print(step)
