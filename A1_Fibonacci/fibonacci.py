def fib_iterative(n):
    a, b, steps, seq = 0, 1, 0, []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
        steps += 1
    return seq, steps  # O(n)


def fib_recursive(n, count):
    count[0] += 1  # every call is one step
    if n < 2:
        return n
    return fib_recursive(n - 1, count) + fib_recursive(n - 2, count)  # O(2^n)


n = int(input("Enter n: "))
seq, steps = fib_iterative(n)
print("Series:", seq)
print("Iterative steps:", steps)

count = [0]
print(f"Recursive fib({n}) =", fib_recursive(n, count), "| steps (calls):", count[0])


# ======================= VIVA QUESTIONS =======================
# Q: What is the Fibonacci series?
# A: Each term is the sum of the previous two: F(n) = F(n-1) + F(n-2), with F(0)=0, F(1)=1.
# Q: Time complexity of the iterative and recursive versions?
# A: Iterative O(n); recursive O(2^n) (tightly O(phi^n), phi = 1.618).
# Q: Space complexity?
# A: Iterative O(1) (O(n) if the series is stored); recursive O(n) for the call stack.
# Q: What do you mean by "computational steps"?
# A: Number of basic operations / function calls executed. Here: loop iterations (iterative) and calls (recursive).
# Q: Why is the recursive version so slow?
# A: Overlapping subproblems - the same F(k) is recomputed many times (fib(10) makes 177 calls).
# Q: Recurrence relation for the recursive step count?
# A: T(n) = T(n-1) + T(n-2) + 1. Number of calls = 2*F(n+1) - 1.
# Q: How can the recursive version be improved?
# A: Memoization / dynamic programming -> O(n); matrix exponentiation or fast doubling -> O(log n).
# Q: Difference between memoization and tabulation?
# A: Memoization = top-down (recursion + cache); tabulation = bottom-up (fill a table iteratively).
# Q: What is dynamic programming?
# A: Solving a problem by storing solutions of overlapping subproblems to avoid recomputation.
# Q: Best case vs worst case?
# A: Same for both versions - the step count depends only on n.
# Q: What does the ratio F(n+1)/F(n) tend to?
# A: The golden ratio, about 1.618.
# Q: Applications of Fibonacci?
# A: Algorithm analysis, Fibonacci heap, Fibonacci search, golden ratio in nature/design, DP demos.
# Q: What does "a, b = b, a + b" do?
# A: Tuple assignment - both right-hand values are evaluated first, so no temp variable is needed.
