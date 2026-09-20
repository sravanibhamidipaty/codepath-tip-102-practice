from collections import deque

# Zombie Spread (Problem Set 1, Problem 5)

"""
Understand
1. What does this grid represent and what are the cell values?
2. How does the infection spread when there are multiple initial zombies?
3. What if no safe human zones exist initially?
4. When do we return -1?

Plan
1. Retrieve grid dimensions R = len(grid) and C = len(grid[0]).
2. Initialize a queue q = deque() and a counter safe_zones = 0.
3. Scan the entire grid:
    - If grid[r][c] == 2, enqueue (r, c) into q.
    - If grid[r][c] == 1, increment safe_zones.
4. Edge Case: If safe_zones == 0, return 0 immediately.
5. Initialize hours = 0 and directional vectors directions = [(-1, 0), (1, 0), (0, -1), (0, 1)].
6. Perform Multi-Source BFS while q is not empty and safe_zones > 0:
    - Increment hours += 1.
    - Snapshot the current queue length size = len(q) to process all zombie zones for the current hour level:
        - Pop r, c = q.popleft().
        - For each (dr, dc) in directions:
            - Calculate neighbor coordinates nr = r + dr, nc = c + dc.
            - If (nr, nc) is in bounds and grid[nr][nc] == 1:
                - Mutate grid[nr][nc] = 2 (infect the zone).
                - Decrement safe_zones -= 1.
                - Enqueue (nr, nc).
7. Return hours if safe_zones == 0 else -1.
"""

# Implement
def time_to_infect(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    q = deque()
    safe_zones = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                safe_zones += 1

    if safe_zones == 0:
        return 0

    hours = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q and safe_zones > 0:
        hours += 1

        for _ in range(len(q)):
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    safe_zones -= 1
                    q.append((nr, nc))

    return hours if safe_zones == 0 else -1

grid_1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

grid_2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]

grid_3 = [[0, 2]]

print(time_to_infect(grid_1))
print(time_to_infect(grid_2))
print(time_to_infect(grid_3))

# TC: O(R x C) where R is the number of rows and C is the number of columns.
#   - Grid Pre-Processing: Iterating through all R x C cells to locate initial zombies and count safe human zones takes O(R x C).
#   - Multi-Source BFS Traversal: Each cell enters and leaves the queue at most once. For every popped cell, checking 4 cardinal directions takes O(1) time. Thus the BFS processes at most R x C cells -> O(R x C).
# SC: O(R x C) where R is the number of rows and C is the number of columns.
#   - Queue (q): In the worst-case scenario (e.g., half the grid filled with zombies initially), the queue holds at most O(R x C) coordinates tuples.
#   - In-Place Mutation: Grid state updates are mutated in-place (grid[nr][nc] = 2), requiring no additional matrix memory.

# Walls and Gates (Problem Set 2, Problem 3)

"""
Understand
1. What does each cell in the grid represent?
2. Why use Multi-Source BFS instead of running BFS from every empty room?

Plan
1. Retrieve grid dimensions R = len(castle) and C = len(castle[0]).
2. Initialize a queue q = deque().
3. Scan the grid to find all gates: if castle[r][c] == 0, append (r, c) to q.
4. Define direction vectors for moving up, down, left, and right: [(-1, 0), (1, 0), (0, -1), (0, 1)].
5. While q is not empty:
    - Pop cell (r, c) = q.popleft().
    - For each neighbor (nr, nc) in 4 directions:
        - Check if (nr, nc) is within bounds and castle[nr][nc] == float('inf').
        - Update distance in-place: castle[nr][nc] = castle[r][c] + 1.
        - Append (nr, nc) to q.
6. Return castle modified in-place.
"""

# Implement
def walls_and_gates(castle):
    if not castle or not castle[0]:
        return castle

    rows = len(castle)
    cols = len(castle[0])
    q = deque()

    for r in range(rows):
        for c in range(cols):
            if castle[r][c] == 0:
                q.append((r, c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols and castle[nr][nc] == float('inf'):
                castle[nr][nc] = castle[r][c] + 1
                q.append((nr, nc))

    return castle

castle = [
    [float('inf'), -1, 0, float('inf')],            # Row 0
    [float('inf'), float('inf'), float('inf'), -1], # Row 1
    [float('inf'), -1, float('inf'), -1],           # Row 2
    [0, -1, float('inf'), float('inf')]             # Row 3
    ]

print(walls_and_gates(castle))

# TC: O(R x C) where R is the number of rows and C is the number of columns.
#   - Finding all gates in Step 1 takes O(R x C) time.
#   - During the multi-source BFS traversal, every empty room is visited and enqueued at most once because its distance changes from float('inf') to a finite number on its first visit.
#   - Processing each queue entry checks 4 constant neighbor directions -> O(1) per cell.
# SC: O(R x C) where R is the number of rows and C is the number of columns.
#   - Queue (q): In the worst case, the queue can hold up to O(R x C) cell coordinates at once.
#   - In-Place Updates: Matrix values are mutated directly in the castle grid without allocating extra auxiliary grids.

# Surrounded Regions (Problem Set 2, Problem 4)

"""
Understand
1. What makes an 'O' region surrounded?
2. Why start from the borders?
3. How do we process the grid?

Plan
1. Check edge cases for empty or 1 x 1 maps.
2. Retrieve matrix dimensions R = len(map) and C = len(map[0])
3. Define a recursive helper function helper(r, c):
    - Base case: If out of bounds or map[r][c] != "O", return.
    - Set map[r][c] = "T".
    - Recursively call helper in all 4 cardinal directions (up, down, left, right).
4. Traverse the outer boundaries (top row, bottom row, left column, right column):
    - For every border cell where map[r][c] == "O", call helper(r, c).
5. Iterate through the entire grid:
    - If map[r][c] == "O", change it to "X".
    - If map[r][c] == "T", restore it to "O".
6. Return map.
"""

# Implement
def capture(map):
    if not map or not map[0]:
        return map

    rows = len(map)
    cols = len(map[0])

    def helper(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or map[r][c] != "O":
            return

        # Mark as temporary safe cell
        map[r][c] = "T"

        # Traverse 4 directional neighbors
        helper(r+1, c)
        helper(r, c+1)
        helper(r, c-1)
        helper(r-1, c)


    # Step 1: Run helper DFS on all border 'O' cells
    for r in range(rows):
        for c in range(cols):
            if map[r][c] == "O" and (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                helper(r, c)

    # Step 2: Final grid update
    for r in range(rows):
        for c in range(cols):
            if map[r][c] == "O":
                map[r][c] = "X"
            elif map[r][c] == "T":
                map[r][c] = "O"

    return map

map = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

print(capture(map))

# TC: O(R x C) where R is the number of rows and C is the number of columns.
#   - Border Scan and DFS Phase: Each cell in the grid is visited at most once during the boundary DFS traversal. Uncapturable cells change to 'T' preventing redundant visits.
#   - Final Grid Sweep: A two-dimensional loop checks every cell once, taking O(R x C) time.
# SC: O(R x C)
#   - Recursion Stack: In the worst-case scenario (e.g., a board filled entirely with 'O's), the recursive call stack for helper can reach a depth of O(R x C).
#   - In-Place Modification: Board state updates are mutated in-place without creating auxiliary grids.