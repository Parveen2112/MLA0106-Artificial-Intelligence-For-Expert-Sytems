def solve(q=[]):
    n = len(q)
    if n == 8:
        for i in q:
            print(" ".join("Q" if j == i else "." for j in range(8)))
        return True
    for col in range(8):
        if all(col != c and abs(col - c) != n - i for i, c in enumerate(q)):
            if solve(q + [col]):
                return True

solve()
