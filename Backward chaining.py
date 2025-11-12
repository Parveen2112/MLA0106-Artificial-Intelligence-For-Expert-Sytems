KB = [
    ("vertebrate(A)", "animal(A)"),
    ("mammal(A)", "vertebrate(A)"),
    ("vertebrate(A),flying(A)", "bird(A)")
]

facts = {"vertebrate('duck')", "flying('duck')", "mammal('cat')"}

def backward_chain(goal):
    if goal in facts:
        return True
    for premise, conclusion in KB:
        if goal in conclusion:
            parts = premise.split(',')
            if all(backward_chain(p.strip()) for p in parts):
                facts.add(goal)
                return True
    return False

goal = "bird('duck')"
print(f"Goal: {goal}")
print("Can be derived?" , backward_chain(goal))
