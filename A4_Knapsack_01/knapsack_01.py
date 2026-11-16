values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)

# dp[i][w] = best value using first i items with capacity w
dp = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(W + 1):
        dp[i][w] = dp[i - 1][w]
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

# trace back chosen items
chosen, w = [], W
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        chosen.append(i)
        w -= weights[i - 1]

print("Maximum value:", dp[n][W])
print("Items chosen:", chosen[::-1])


# ======================= VIVA QUESTIONS =======================
# Q: What is the 0/1 knapsack problem?
# A: Choose a subset of items (each taken entirely or not at all) with total weight <= W and maximum value.
# Q: Write the DP recurrence.
# A: dp[i][w] = dp[i-1][w] if wt[i] > w, else max(dp[i-1][w], val[i] + dp[i-1][w - wt[i]]).
# Q: Base cases?
# A: dp[0][w] = 0 and dp[i][0] = 0.
# Q: Time and space complexity?
# A: O(n*W) for both. This is pseudo-polynomial (depends on the numeric value of W).
# Q: How to reduce space?
# A: Use a 1-D array and iterate w from W down to wt[i] -> O(W) space (but traceback becomes harder).
# Q: Why not greedy?
# A: Items cannot be split, so best-ratio-first can leave wasted capacity (greedy gives 160, DP gives 220).
# Q: Optimal substructure and overlapping subproblems here?
# A: The optimal answer for (i, w) is built from optimal answers for (i-1, ...); the same (i, w) states repeat.
# Q: How do you find which items were chosen?
# A: Trace back from dp[n][W]: if dp[i][w] != dp[i-1][w], item i was taken, then w -= wt[i].
# Q: Explain branch and bound for knapsack.
# A: Build a state-space tree (include/exclude each item), compute an upper bound with the fractional knapsack,
#    and prune nodes whose bound <= best known value. Worst case O(2^n) but usually much faster.
# Q: DP vs branch and bound?
# A: DP is pseudo-polynomial and needs integer weights; B&B works for any weights but is exponential in the worst case.
# Q: Is knapsack NP-complete?
# A: The decision version is NP-complete (weakly - it has a pseudo-polynomial solution).
# Q: 0/1 vs unbounded knapsack?
# A: Unbounded allows unlimited copies of each item.
# Q: What if weights are fractions?
# A: Scale them to integers or use branch and bound.
# Q: Applications?
# A: Budgeting, resource allocation, cargo loading, project selection.
# Q: Your output?
# A: Max value 220, taking items 2 and 3 (weights 20+30 = 50, values 100+120).
