items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50

items.sort(key=lambda x: x[0] / x[1], reverse=True)  # greedy: best value/weight ratio first
total = 0
for value, weight in items:
    if capacity >= weight:
        total += value
        capacity -= weight
    else:
        total += value * capacity / weight  # take fraction of the last item
        break

print("Maximum value:", total)


# ======================= VIVA QUESTIONS =======================
# Q: What is the fractional knapsack problem?
# A: Given items with value and weight and a bag of capacity W, maximize total value; items can be broken into fractions.
# Q: What is the greedy criterion?
# A: Highest value/weight ratio first; take whole items while they fit, then a fraction of the next one.
# Q: Why does greedy work here but not for 0/1 knapsack?
# A: Because items are divisible, the bag can always be filled completely with the best-ratio material.
# Q: Counter-example where greedy fails for 0/1?
# A: Items (60,10), (100,20), (120,30), W=50: greedy by ratio gives 160, the optimal 0/1 answer is 220.
# Q: Time complexity?
# A: O(n log n) for sorting + O(n) for the loop. Extra space O(1).
# Q: Why not sort by value only or weight only?
# A: Neither accounts for value per unit of capacity, so the result may not be optimal.
# Q: Is the problem NP-hard?
# A: Fractional is solvable in polynomial time; 0/1 knapsack is NP-hard.
# Q: Explain your output (240).
# A: Take 60 (w=10) + 100 (w=20) = 160, remaining capacity 20 -> 20/30 of the 120 item = 80. Total = 240.
# Q: What if total weight <= capacity?
# A: Take every item (the else branch is never reached).
# Q: Can the time be improved?
# A: Yes - use a max-heap or the weighted-median method for O(n).
# Q: What are feasible and optimal solutions?
# A: Feasible = total weight <= W; optimal = feasible solution with maximum value.
# Q: Applications?
# A: Cargo loading, resource/budget allocation, cutting stock, portfolio selection.
