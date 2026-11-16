jobs = [("a", 2, 100), ("b", 1, 19), ("c", 2, 27), ("d", 1, 25), ("e", 3, 15)]  # (id, deadline, profit)

jobs.sort(key=lambda j: j[2], reverse=True)  # greedy: highest profit first
slots = [None] * max(j[1] for j in jobs)

for name, deadline, profit in jobs:
    for t in range(deadline - 1, -1, -1):  # latest free slot on/before deadline
        if slots[t] is None:
            slots[t] = (name, profit)
            break

done = [s for s in slots if s]
print("Job sequence:", [s[0] for s in done])
print("Total profit:", sum(s[1] for s in done))


# ======================= VIVA QUESTIONS =======================
# Q: State the job sequencing problem with deadlines.
# A: n jobs, each with a deadline and profit, each takes 1 unit of time on one machine. Pick a feasible subset
#    and order it so every job finishes by its deadline and total profit is maximum.
# Q: What is the greedy strategy used?
# A: Sort jobs by profit (descending); place each job in the latest free slot on or before its deadline;
#    skip the job if no slot is free.
# Q: Why search the slot backwards from the deadline?
# A: Using the latest free slot keeps earlier slots free for jobs with tighter deadlines.
# Q: Why does greedy give the optimal answer?
# A: Greedy-choice property + exchange argument: swapping in a higher-profit job never reduces total profit.
# Q: Time complexity?
# A: Sorting O(n log n) + slot search O(n*d) -> O(n^2) worst case. With Disjoint Set Union it is ~O(n log n).
# Q: Space complexity?
# A: O(d) for the slots array, d = maximum deadline.
# Q: What is a feasible set of jobs?
# A: A set in which all jobs can be scheduled so that each meets its deadline.
# Q: What if two jobs have the same profit?
# A: Either can be chosen first; total profit stays the same but the sequence may differ.
# Q: Is the output sequence unique?
# A: Maximum profit is unique; the job order may not be.
# Q: How is it different from activity selection?
# A: Activity selection maximizes the NUMBER of jobs (sorted by finish time); here we maximize PROFIT with unit-time jobs.
# Q: Greedy vs dynamic programming?
# A: Greedy makes a locally optimal choice and never reconsiders; DP solves all subproblems and combines them.
# Q: What if jobs take different time units?
# A: The problem becomes NP-hard; this greedy method no longer guarantees optimality.
# Q: Applications?
# A: CPU/task scheduling, manufacturing, project planning, ad slot allocation.
# Q: Explain your output.
# A: c (deadline 2) -> slot 1, a (deadline 2) -> slot 2, e (deadline 3) -> slot 3; b and d are dropped.
#    Profit = 27 + 100 + 15 = 142.
