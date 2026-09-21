# Mewtwo's Genetic Fusion (Problem Set 2, Problem 6)

"""
Understand
1. What is the length requirement?
2. How should the characters be ordered?

Plan
1. Let m = len(dna1) and n = len(dna2).
2. If m + n is not equal to len(dna3), return False.
3. Create a 2D boolean DP grid dp of dimensions (m+1) x (n+1) where dp[i][j] represents whether dna3[:i+j] can be formed by interleaving dna1[:i] and dna2[:j].
4. Base Case: dp[0][0] = True (two empty strings interleave to form an empty string).
5. Fill First Column (j = 0): dp[i][0] is True if dp[i-1][0] is True and dna1[i-1] == dna3[i-1].
6. Fill First Row (i = 0): dp[0][j] is True if dp[0][j-1] is True and dna2[j-1] == dna3[j-1].
7. Fill Rest of DP Table: For each cell (i, j): dp[i][j] is True if it comes from above (dp[i-1][j] is True and dna1[i-1] == dna3[i+j-1]) OR if it comes from the left (dp[i][j-1] is True and dna2[j-1] == dna3[i+j-1]).
8. Return dp[m][n].
"""

# Implement
def genetic_fusion(dna1, dna2, dna3):
    m = len(dna1)
    n = len(dna2)

    if m + n != len(dna3):
        return False

    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True

    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] and dna1[i-1] == dna3[i-1]

    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] and dna2[j-1] == dna3[j-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            match_dna1 = dp[i-1][j] and dna1[i-1] == dna3[i+j-1]
            match_dna2 = dp[i][j - 1] and dna2[j - 1] == dna3[i + j - 1]
            dp[i][j] = match_dna1 or match_dna2

    return dp[m][n]

print(genetic_fusion("aabcc", "dbbca", "aadbbcbcac"))
print(genetic_fusion("aabcc", "dbbca", "aadbbbaccc"))
print(genetic_fusion("", "", ""))

# TC: O(m x n) where m is len(dna1) and n is len(dna2). Filling each cell in the (m+1) x (n+1) DP table takes constant O(1) time.
# SC: O(m x n) where m is len(dna1) and n is len(dna2). Requires an (m + 1) x (n + 1) 2D array.

# Toph and Katara's Training Synchronization (Problem Set 1, Problem 6)

"""
Understand
1. What is a subsequence?
2. What are we looking for?

Plan
1. Get string length m = len(katara_moves) and n = len(toph_moves)
2. Create a 2D DP matrix dp of size (M + 1) x (N + 1) filled with 0.
3. Iterate i from 1 to m and j from 1 to n.
    - If katara_moves[i-1] == toph_moves[j-1]:
        - dp[i][j] = 1 + dp[i-1][j-1] (Diagonal transition: match found).
    - Else:
        - dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (Max of skipping a character from Katara vs. Toph).
4. Return dp[m][n]
"""

# Implement
def training_synchronization(katara_moves, toph_moves):
    m = len(katara_moves)
    n = len(toph_moves)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if katara_moves[i-1] == toph_moves[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

print(training_synchronization("waterbend", "earthbend"))
print(training_synchronization("bend", "bend"))
print(training_synchronization("fire", "air"))

# TC: O(m x n) where m is the length of katara_moves and n is the length of toph_moves. We fill an (m+1) x (n+1) DP grid where each cell takes O(1) constant time work.
# SC: O(m x n) where m is the length of the katara_moves and n is the length of toph_moves. It requires an (m+1) x (n+1) 2D matrix to store the dynamic programming states.

# Zuko's Redemption Mission (Problem Set 1, Problem 5)

"""
Understand
1. What is the objective?
    - Find the minimum number of supply tokens that sum up to exactly amount.
2. What if it's impossible to reach amount?
    - Return -1
3. What is the base case?
    - amount == 0 requires 0 tokens -> dp[0] = 0.

Plan
1. Create 1D DP array dp of size amount + 1 initialized with float('inf') to represent uncalculated states.
2. Set base case: dp[0] = 0.
3. Loop through every target value i from 1 to amount:
    - For each token in tokens:
        - If i - token >= 0, update: dp[i] = min(dp[i], 1 + dp[i-token]).
4. If dp[amount] is still float('inf'), return -1. Otherwise return dp[amount].
"""

# Implement
def zuko_supply_mission(tokens, amount):
    # dp[i] will store the minimum tokens needed to reach supply amount i
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 supplies require 0 to tokens
    dp[0] = 0

    for i in range(1, amount+1):
        for token in tokens:
            if i - token >= 0:
                dp[i] = min(dp[i], 1 + dp[i-token])

    return dp[amount] if dp[amount] != float('inf') else -1

print(zuko_supply_mission([1, 2, 5], 11))
print(zuko_supply_mission([2], 3))
print(zuko_supply_mission([1], 0))

# TC: O(A x N) where A is the target amount and N is the number of token types. We iterate through all amounts from 1 to A. For each amount, we iterate through all N tokens to find the minimum transition.
# SC: O(A) because it requires a 1D array dp of size A + 1 to store intermediate minimum token counts.