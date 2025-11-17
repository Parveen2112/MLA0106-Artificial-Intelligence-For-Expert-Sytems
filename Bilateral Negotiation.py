T=100; dA=0.9; dB=0.85; R=10

def nego():
    A="A"
    for r in range(R):
        if A=="A":
            a=int(T*dA**r); b=T-a
            if b*dB**r >= (T/2)*dB**r: return "A",a,b,r
            A="B"
        else:
            b=int(T*dB**r); a=T-b
            if a*dA**r >= (T/2)*dA**r: return "B",a,b,r
            A="A"
    return None

res=nego()
if res:
    p,a,b,r=res
    print("Proposer:",p,"\nA:",a,"B:",b,"Rounds:",r)
    print("Fair?", abs(a*dA**r - b*dB**r)<5)
else:
    print("No deal")
