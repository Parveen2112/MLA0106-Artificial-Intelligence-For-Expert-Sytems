import random

def cost(s):
    return sum(1 for i in range(len(s)) for j in range(i+1,len(s))
               if s[i]==s[j] or abs(s[i]-s[j])==abs(i-j))

def hill_climb(n=8):
    s=[random.randint(0,n-1) for _ in range(n)]
    while True:
        c=cost(s)
        neigh=[(s[:i]+[r]+s[i+1:],cost(s[:i]+[r]+s[i+1:])) 
               for i in range(n) for r in range(n) if r!=s[i]]
        best=min(neigh,key=lambda x:x[1])
        if best[1]<c: s=best[0]
        else: return s,c

b,c=hill_climb(8)
for i in range(8): print(" ".join("Q" if b[j]==i else "." for j in range(8)))
print("Final Cost:",c, "✅" if c==0 else "❌")
