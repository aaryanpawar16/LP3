def binomial(n, k):
    C = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Pascal's rule: C(i,j) = C(i-1,j-1) + C(i-1,j)
            C[i][j] = 1 if j == 0 or j == i else C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]


n, k = int(input("n: ")), int(input("k: "))
print(f"C({n},{k}) =", binomial(n, k))


# ======================= VIVA QUESTIONS =======================
# Q: What is a binomial coefficient?
# A: C(n,k) = n! / (k! (n-k)!), the number of ways to choose k items from n.
# Q: Recurrence used?
# A: Pascal rule: C(n,k) = C(n-1,k-1) + C(n-1,k), with C(n,0) = C(n,n) = 1.
# Q: Why dynamic programming?
# A: Plain recursion recomputes the same C(i,j) repeatedly (exponential); DP stores each value once.
# Q: Time and space complexity?
# A: O(n*k) time, O(n*k) space; O(k) space is possible using one row.
# Q: Why does the loop run j up to min(i, k)?
# A: C(i,j) = 0 for j > i, and we never need columns beyond k.
# Q: Relation to Pascal's triangle?
# A: Row n, entry k of Pascal's triangle is C(n,k).
# Q: Useful properties?
# A: C(n,k) = C(n,n-k); sum of row n = 2^n; C(n,0) = 1.
# Q: Why not just use factorials?
# A: Factorials overflow quickly in fixed-size ints; the DP only does additions.
# Q: Faster alternative?
# A: Multiplicative formula C(n,k) = product of (n-k+i)/i for i = 1..k, in O(k).
# Q: Memoization vs tabulation?
# A: Memoization = top-down recursion with a cache; tabulation = bottom-up table (used here).
# Q: Applications?
# A: Binomial theorem (a+b)^n, probability, combinatorics, counting paths in a grid.
# Q: What does the code return when k > n?
# A: 0, because that cell is never filled.
# Q: Where are overlapping subproblems and optimal substructure?
# A: C(i,j) depends on C(i-1,j-1) and C(i-1,j) (substructure), shared by many cells (overlap).
