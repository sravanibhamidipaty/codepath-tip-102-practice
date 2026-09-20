# Celebrity Feuds (Problem Set 2, Problem 8)

"""
Understand
1. What does it mean to split celebrities into two arrival groups?
2. How is this represented as a graph problem?
3. How do 1-based labels impact implementation?

Plan
1. Build the Graph:
    - Create an adjacency list graph of size n + 1.
    - For each pair [a, b] in dislikes, add an undirected edge: graph[a].append(b) and graph[v].append(u).
2. Initialize Coloring:
    - Create a colors array of size n + 1 initialized to 0 (0: uncolored, 1: Group A, -1: Group B).
3. Define Helper DFS Function dfs(node, node_color):
    - Assign colors[node] = node_color.
    - For each neighbor in graph[node]:
        - If colors[neighbor] == node_color, a coloring conflict is found -> return False.
        - If colors[neighbor] == 0 and not dfs(neighbor -node_color), recursive coloring failed -> return False.
    - If no conflict occur, return True.
4. Process Graph Components:
    - Loop node_idx from 1 to n.
    - If colors[node_idx] == 0, start a DFS from node_idx with initial color 1. If it fails, return False.
5. Return Result:
    - If all components are successfully colored with two colors, return True.
"""

# Implement
def can_split(n, dislikes):
    graph = [[] for _ in range(n+1)]

    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n+1)

    def dfs(node, node_color):
        colors[node] = node_color

        for neighbor in graph[node]:
            if colors[neighbor] == node_color:
                return False

            if colors[neighbor] == 0 and not dfs(neighbor, -node_color):
                return False

        return True


    for node_idx in range(1, n+1):
        if colors[node_idx] == 0 and not dfs(node_idx, 1):
            return False

    return True

dislikes_1 = [[1, 2], [1, 3], [2, 4]]
dislikes_2 = [[1, 2], [1, 3], [2, 3]]

print(can_split(4, dislikes_1))
print(can_split(3, dislikes_2))

# TC: O(V + E) where V is the number of celebrities (nodes) and E = len(dislikes) is the number of dislike pairs (edges).
#   - Graph Construction: Building the adjacency list iterates through E dislike pairs, taking O(E) time.
#   - DFS Traversal: The DFS traversal visits each vertex once, taking O(V) time. For each vertex, we iterate through
#   all its adjacent vertices (edges), which across all vertices takes O(E) time.
# SC: O(V + E) where V is the number of celebrities (nodes) and E = len(dislikes) is the number of dislike pairs (edges).
#   - Adjacency List: Storing the graph representation requires O(V + E) space.
#   - Color Array: Stores the color for each vertex: O(V) space.
#   - Recursion Stack: In the worst-case (a single linear chain of dislikes), the recursive call stack can reach a depth of O(V).

# Gossip Chain (Problem Set 2, Problem 5)

"""
Understand
1. What should the default value be for unreachable vertices?
2. If a celebrity has multiple out-neighbors, does the traversal order matter?

Plan
1. Initialize an adjacency list graph using a dictionary to map who passes gossip to whom.
2. Collect all unique celebrities into a set to initialize our output mapping with default values of (-1, "-1").
3. Sort each celebrity's neighbor list alphabetically to ensure order consistency.
4. Establish a global tracking state: a time integer starting at 1 and a visited set.
5. Create a recursive dfs(node) helper function:
    - Add the node to visited.
    - Record its arrival_time = time
    - Increment time by 1.
    - Loop through sorted neighbors: if a neighbor hasn't been visited, recursively call dfs(neighbor).
    - After handling all neighbors, record its departure_time = time.
    - Increment time by 1.
    - Save the tuple (arrival_time, departure_time) in the results dictionary.
6. Initiate dfs(start) if the start person exists, then return the results.
"""

from collections import defaultdict

# Implement
def rumor_spread_times(connections, n, start):
    # Step 1: Build adjacency list and discover all individual celebrities
    graph = defaultdict(list)
    all_celebs = set()

    for u, v in connections:
        graph[u].append(v)
        all_celebs.add(u)
        all_celebs.add(v)

    # Sort neighbors for deterministic execution order
    for node in graph:
        graph[node].sort()

    # Step 2: Set default baseline metrics for unreached celebrities
    result = {celeb: (-1, -1) for celeb in all_celebs}

    time = 1
    visited = set()

    def dfs(node):
        nonlocal time
        visited.add(node)
        arrival = time
        time += 1

        # Traverse through sorted neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        departure = time
        time += 1
        result[node] = (arrival, departure)

    # Step 3: Run the traversal from the source node
    if start in all_celebs:
        dfs(start)

    return result

connections = [
    ["Amber Gill", "Greg O'Shea"],
    ["Amber Gill", "Molly-Mae Hague"],
    ["Greg O'Shea", "Molly-Mae Hague"],
    ["Greg O'Shea", "Tommy Fury"],
    ["Molly-Mae Hague", "Tommy Fury"],
    ["Tommy Fury", "Ovie Soko"],
    ["Curtis Pritchard", "Maura Higgins"]
]

print(rumor_spread_times(connections, 7, "Amber Gill"))

# TC: O(V + E log (E/V)) where V is unique celebrities and E is connections. Building graph and DFS takes O(V+E).
# Sorting neighbors takes O(E log(Degree)).
# SC: O(V + E) to store the adjacency list structure, visited tracker, and call stack frame up to O(V).

"""
Execution Dry Run
Adjacency List Construction (Sorted)
- Amber Gill: ["Greg O'Shea", "Molly-Mae Hague"]
- Greg O'Shea: ["Molly Mae Hague", "Tommy Fury"]
- Molly-Mae Hague: ["Tommy Fury"]
- Tommy Fury: ["Ovie Soko"]
- Curtis Pritchard: ["Maura Higgins"]
- Unlisted as sources (no neighbors): Ovie Soko, Maura Higgins

DFS Timeline Tracing
1. dfs("Amber Gill")
    1. time is 1. "Amber Gill" arrival = 1.
    2. time increments to 2.
    3. Neighbor 1: "Greg O'Shea" (unvisited) -> Call dfs("Greg O'Shea")
2. dfs("Greg O'Shea")
    1. time is 2. "Greg O'Shea" arrival = 2.
    2. time increments to 3.
    3. Neighbor 1: "Molly-Mae Hague" (unvisited) -> Call dfs("Molly-Mae Hague")
3. dfs("Molly-Mae Hague")
    1. time is 3. "Molly-Mae Hague" arrival = 3.
    2. time increments to 4.
    3. Neighbor 1: "Tommy Fury" (unvisited) -> Call dfs("Tommy Fury")
4. dfs("Tommy Fury")
    1. time is 4. "Tommy Fury" arrival 4.
    2. time increments to 5.
    3. Neighbor 1: "Ovie Soko" (unvisited) -> Call dfs("Ovie Soko")
5. dfs("Ovie Soko")
    1. time is 5. "Ovie Soko" arrival = 5.
    2. time increments to 6.
    3. Neighbor loop: None.
    4. "Ovie Soko" departure = 6.
    5. time increments to 7.
    6. Returns back to dfs("Tommy Fury").
6. Resume dfs("Tommy Fury")
    1. Neighbor loop: Completed.
    2. "Tommy Fury" departure = 7.
    3. time increments to 8.
    4. Returns back to dfs("Molly-Mae Hague").
7. Resume dfs("Molly-Mae Hague")
    1. Neighbor loop: Completed.
    2. "Molly-Mae Hague" departure = 8.
    3. time increments to 9.
    4. Returns back to dfs("Greg O'Shea").
8. Resume dfs("Greg O'Shea")
    1. Neighbor 2: "Tommy Fury" -> Checked but already inside visited set. Loop done.
    2. "Greg O'Shea" departure = 10.
    3. time increments 11.
    4. Returns back to dfs("Amber Gill").
9. Resume dfs("Amber Gill")
    1. Neighbor 2: "Molly-Mae Hague" → Checked but already inside visited set. Loop done.
    2. "Amber Gill" departure = 11.
    3. time increments to 12.
    4. DFS processing concludes.
10. Disconnected Nodes Check
    1. Curtis Pritchard and Maura Higgins were never hit by the recursive path. They retain their initialization default 
    values of (-1, "-1").
"""

# Network Strength (Problem Set 2, Problem 6)

"""
Understand
1. What defines a "strongly connected" group in this problem?
2. How do we check this efficiently?

Plan
1. Extract the full set of celebrities: all_celebs = set(celebrities.keys()).
2. Iterate through each person and their list of likes in celebrities:
    a. Create expected liked set: expected_likes = all_celebs - {person}.
    b. Convert likes list to a set actual_likes.
    c. If actual_likes != expected_likes, return False.
3. If all celebrities pass the check, return True.
"""

# Implement
def is_strongly_connected(celebrities: dict[str, list[str]]) -> bool:
    all_celebs = set(celebrities.keys())

    for person, likes in celebrities.items():
        expected_likes = all_celebs - {person}
        actual_likes = set(likes)

        if actual_likes != expected_likes:
            return False

    return True
celebrities1 = {
    "Dev Patel": ["Meryl Streep", "Viola Davis"],
    "Meryl Streep": ["Dev Patel", "Viola Davis"],
    "Viola Davis": ["Meryl Streep", "Dev Patel"]
}

celebrities2 = {
    "John Cho": ["Rami Malek", "Zoe Saldana", "Meryl Streep"],
    "Rami Malek": ["John Cho", "Zoe Saldana", "Meryl Streep"],
    "Zoe Saldana": ["Rami Malek", "John Cho", "Meryl Streep"],
    "Meryl Streep": []
}

print(is_strongly_connected(celebrities1))  # Output: True
print(is_strongly_connected(celebrities2))  # Output: False

# TC: O(V + E) where V is the number of celebrities (nodes) and E is the total number of likes (edges).
#   - Extracting Keys & Set Operations: Creating all_celebs takes O(V) time.
#   - Traversing Adjacency List: Converting each likes list into a set takes time proportional to its length. Across all celebrities, set conversions process E edges in total.
# SC: O(V)
#   - all_celebs Set: Stores V unique celebrity names requiring O(V) auxiliary space.
#   - expected_likes / actual_likes Sets: Bounded by O(V) space per iteration.