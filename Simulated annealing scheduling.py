import random, math

# --- Problem Setup ---
tasks = ["T1","T2","T3","T4","T5","T6"]
time_slots = [0,1,2]   # 3 slots

# Cost = number of tasks exceeding slot capacity (max 2 per slot)
def cost(schedule):
    slot_count = {0:0,1:0,2:0}
    for t in schedule:
        slot_count[t] += 1
    return sum(max(0, slot_count[s] - 2) for s in slot_count)

# Random neighbor = move one task to another slot
def neighbor(schedule):
    new = schedule[:]
    i = random.randint(0, len(tasks)-1)
    new[i] = random.choice(time_slots)
    return new

# --- Simulated Annealing ---
T = 10          # starting temperature
cool = 0.95     # cooling rate
schedule = [random.choice(time_slots) for _ in tasks]
best = schedule[:]

while T > 0.01:
    new = neighbor(schedule)
    c_old, c_new = cost(schedule), cost(new)
    if c_new < c_old or random.random() < math.exp(-(c_new - c_old)/T):
        schedule = new[:]
        if cost(schedule) < cost(best):
            best = schedule[:]
    T *= cool

# --- Output ---
print("Best Schedule:", best)
print("Best Cost:", cost(best))
