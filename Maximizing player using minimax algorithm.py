import math

def minimax(depth, node, isMax, scores, h):
    if depth == h:
        return scores[node]
    if isMax:
        return max(minimax(depth+1, node*2, False, scores, h),
                   minimax(depth+1, node*2+1, False, scores, h))
    else:
        return min(minimax(depth+1, node*2, True, scores, h),
                   minimax(depth+1, node*2+1, True, scores, h))

scores = [3, 5, 2, 9]   # final leaf values
h = math.log2(len(scores))
best = minimax(0, 0, True, scores, int(h))
print("Best value for maximizing player:", best)
