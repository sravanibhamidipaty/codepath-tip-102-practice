# Zombie Infested City Regions (Problem Set 1, Problem 3)

"""
Understand
1. What does the input grid represent?
2. Why upscale 1 x 1 square to 3 x 3?
    - Diagonal lines touch at corners in a standard grid, making 4-directional traversal unable to distinguish whether regions are separated or connected without crossing diagonal walls.
    - Expanding each cell to 3 x 3 creates thick wall boundaries (1s) that cleanly separate open regions (0s) using standard 4-directional DFS or BFS.
3. How do we count the contiguous regions?

Plan
1. Retrieve original grid dimension n = len(grid)
2. Construct a 3n x 3n grid grid2 initialized with 0s.
3. Map each 1 x 1 cell (r, c) from grid to a 3 x 3 block in grid2 starting at (r2, c2) = (r x 3, c x 3):
    - If grid[r][c] == "/": mark anti-diagonal cells (r2, c2+2), (r2+1, c2+1), and (r2+2, c2) as 1.
    - If grid[r][c] == "\\" mark main-diagonal cells (r2, c2), (r2+1, c2+1), and (r2+2, c2+2) as 1.
4. Define a recursive helper dfs(r, c, visited):
    - Base Case: Return if (r, c) is out of bounds, grid2[r][c] == 1 (fence), or (r, c) is in visited.
    - Add (r, c) to visited.
    - Recursively call dfs on the 4 cardinal directions: up, down, left, right.
5. Traverse all cells in grid2:
    - If grid2[r][c] == 0 and (r, c) has not been visited, run dfs(r, c, visited) and increment regions_count += 1.
6. Return regions_count.
"""

# Implement
def count_regions(grid):
    n = len(grid)
    size2 = n * 3
    grid2 = [[0] * size2 for _ in range(size2)]

    # Step 1: Upscale grid to 3x3 per cell to model fence barriers
    for r in range(n):
        for c in range(n):
            r2 = r * 3
            c2 = c * 3
            if grid[r][c] == "/":
                grid2[r2][c2 + 2] = 1
                grid2[r2 + 1][c2 + 1] = 1
                grid2[r2 + 2][c2] = 1
            elif grid[r][c] == "\\":
                grid2[r2][c2] = 1
                grid2[r2 + 1][c2 + 1] = 1
                grid2[r2 + 2][c2 + 2] = 1

    # Step 2: DFS Helper to traverse open regions
    def dfs(r, c, visited):
        if (
            not (0 <= r < size2 and 0 <= c < size2)
            or grid2[r][c] == 1
            or (r, c) in visited
        ):
            return

        visited.add((r, c))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dr, dc in directions:
            dfs(r + dr, c + dc, visited)

    regions_count = 0
    visited = set()

    # Step 3: Count connected components of 0s
    for r in range(size2):
        for c in range(size2):
            if grid2[r][c] == 0 and (r, c) not in visited:
                dfs(r, c, visited)
                regions_count += 1

    return regions_count

grid_1 = [" /","/ "]
print(count_regions(grid_1))

grid_2 = [" /","  "]
print(count_regions(grid_2))

# TC: O(n^2) where n is the side length of the n x n input grid.
#   - Grid Expansion: Populating the 3n x 3n grid iterates through n^2 input cells, performing O(1) coordinate assignments per cell -> O(n^2).
#   - Connected Component DFS: The total size of grid2 is (3n)^2 = 9n^2. Every cell enters visited and is processed at most once during the DFS traversal -> O(n^2).
# SC: O(n^2) where n is the side length of the n x n input grid.
#   - Upscaled Grid (grid2): Stores a 3n x 3n matrix requiring O(n^2) memory.
#   - Visited Tracker (visited): Stores at most 9n^2 coordinate tuples -> O(n^2).
#   - Recursion Stack: In the worst-case open grid, the call stack for dfs reaches a maximum depth of O(n^2).

# Decreasing Zombie Path (Problem Set 1, Problem 5)

"""
Understand
1. What is a valid step?
2. Where can the path start and end?

Plan
1. Retrieve grid dimensions rows = len(cit) and cols = len(city[0]).
2. Initialize a 2D memoization table memo with size rows x cols filled with 0s (or a hash map).
3. Define a recursive helper function dfs(r, c):
    - If memo[r][c] > 0, return memo[r][c] immediately.
    - Set initial path length max_len = 1 (a single cell has a path of length 1).
    - Check all 4 cardinal directions: (-1, 0), (1, 0), (0, -1), (0, 1).
    - If neighbor (nr, nc) is within bounds and city[nr][nc] < city[r][c]:
        - Update max_len = max(max_len, 1 + dfs(nr, nc)).
    - Store memo[r][c] = max_len and return max_len.
4. Iterate through every cell (r, c) in the city grid, calling dfs(r, c), and keep track of the overall maximum length found.
5. Return the overall maximum length.
"""

# Implement
def longest_decreasing_path(city):
    if not city or not city[0]:
        return 0

    rows = len(city)
    cols = len(city[0])
    memo = [[0]*cols for _ in range(rows)]

    def dfs(r, c):
        if memo[r][c] > 0:
            return memo[r][c]

        max_len = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols and city[nr][nc] < city[r][c]:
                max_len = max(max_len, 1+dfs(nr, nc))

        memo[r][c] = max_len
        return max_len

    longest = 0
    for r in range(rows):
        for c in range(cols):
            longest = max(longest, dfs(r, c))

    return longest

city_1 = [
    [4, 3],
    [1, 2]
]

city_2 = [
    [1, 2, 18, 3],
    [26, 6, 7, 15],
    [9, 10, 17, 18],
    [14, 15, 16, 22]
]

print(longest_decreasing_path(city_1))
print(longest_decreasing_path(city_2))

# TC: O(M x N) where M is the number of rows and N is the number of columns.
#   - With memoization, dfs(r, c) is computed at most once for each cell.
#   - For each cell, we check its 4 cardinal neighbors, taking O(1) constant time.
# SC: O(M x N)
#   - Memoization Grid (memo): Requires an M x N matrix to store intermediate path lengths.
#   - Recursion Call Stack: In the worst-case scenario (where the matrix contains a snake-like strictly decreasing path visiting every cell), the DFS call stack depth reaches O(M x N).

# Defending the Safehouse (Problem Set 1, Problem 2)

"""
Understand
1. What are the movement rules?
    - You can only move right (r, c+1) or down (r+1, c).
2. What does disconnecting mean?
    - Removing all valid paths from (0, 0) to (m-1, n-1) by setting at most one cell value from 1 to 0 (excluding the start and end cells).

Key Insights:
    - If there is already no path from start to end, the city is already disconnected -> return True.
    - If there is path, flipping 1 cell can only disconnect the grid if all possible paths pass through at least one common bottleneck cell.
    - If we find one path and destroy/block all its intermediate cells, a second DFS run will tell us if another independent path exists:
        - If a second path exists, 1 flip is NOT enough to break all paths -> return False.
        - If no second path exists, blocking the bottleneck on the first path was enough -> return True.

Plan
1. Define a DFS function dfs(r, c) that searches for a path to (m-1, n-1) moving right and down.
2. During DFS, mark visited cells as 0 to invalidate them.
3. First Run: Run dfs(0, 0) to find the first path from entrance to safehouse.
    - If dfs(0, 0) returns False, return True immediately (already disconnected).
4. Restore the entrance cell city[0][0] = 1 (since the entrance cannot be flipped). Note that cells along the first path (except start and end) remain blocked as 0.
5. Second Run: Run dfs(0, 0) a second time.
    - If dfs(0, 0) return True, another independent path exists -> return False.
    - If dfs(0, 0) returns False, no alternative path exists -> return True.
"""

# Implement
def can_disconnect_safehouse(city):
    if not city or not city[0]:
        return True

    rows = len(city)
    cols = len(city[0])

    def dfs(r, c):
        # Base Case: Reached the safehouse
        if r == rows - 1 and c == cols - 1:
            return True

        # Base Case: Out of bounds or blocked passage
        if not (0 <= r < rows and 0 <= c < cols) or city[r][c] == 0:
            return False

        # Mark cell as visited/blocked
        city[r][c] = 0

        # Try moving Right or Down
        if dfs(r, c+1) or dfs(r+1, c):
            return True

        return False

    # Step 1: First DFS check
    if not dfs(0, 0):
        return True # Already disconnected

    # Step 2: Restore start cell entrance so second DFS can begin
    city[0][0] = 1

    # Step 3: Second DFS check for an alternative path
    has_second_path = dfs(0, 0)

    # If no second path exists, 1 flip was sufficient
    return not has_second_path

city_1 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]

city_2 = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]

print(can_disconnect_safehouse(city_1))
print(can_disconnect_safehouse(city_2))

# TC: O(M x N) where M is the number of rows and N is the number of columns in city.
# We run DFS at most 2 times. Each cell in visited at most once per DFS run because visited cells are mutated to 0. Checking 2 cardinal directions takes O(1) time per cell.
# SC: O(M x N) where M is the number of rows and N is the number of columns in city.
#   - Recursion Stack: In the worst-case scenario, the call stack for recursive DFS reaches a depth equal to the longest path length bounded by O(M x N).
#   - In-Place Mutation: Grid state modifications are made directly on city without extra matrix allocations.