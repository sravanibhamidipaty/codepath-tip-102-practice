from collections import deque

# Copy Seating Chart (Problem Set 2, Problem 8)

"""
Understand
1. What is the input structure?
2. What is the required output?
3. How do we handle edge cases, cycles, and multi-parent references?

Plan
1. Check base edge case: If seat is None, return None.
2. Initialize a hash map graph_copy = {} to map original node instances to their corresponding cloned instances.
3. Pre-create the root clone graph_copy[seat] = Node(seat.val, []).
4. Initialize a BFS queue q = deque([seat]).
5. While q is not empty:
    a. Pop the current original node node = q.popleft().
    b. Iterate through each neighbor in node.neighbors:
        i. If neighbor is not in graph_copy:
            - Clone it: graph_copy[neighbor] = Node(neighbor.val, [])
            - Enqueue original neighbor to q for future expansion.
        ii. Connect the edge in the cloned graph:
            - Append graph_copy[neighbor] to graph_coopy[node].neighbors.
            
6. Return graph_copy[seat]
"""

# Implement
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def compare_graphs(node1, node2, visited=None):
    if visited is None:
        visited = set()

    if node1.val != node2.val:
        return False

    visited.add(node1)

    if len(node1.neighbors) != len(node2.neighbors):
        return False

    for n1, n2 in zip(node1.neighbors, node2.neighbors):
        if n1 not in visited and not compare_graphs(n1, n2, visited):
            return False

    return True

def copy_seating(seat):
    if not seat:
        return None
    graph_copy = {}
    q = deque([seat])

    while q:
        node = q.popleft()

        if node not in graph_copy:
            graph_copy[node] = Node(node.val, [])

        for neighbor in node.neighbors:
            if neighbor not in graph_copy:
                graph_copy[neighbor] = Node(neighbor.val, [])
                q.append(neighbor)
            graph_copy[node].neighbors.append(graph_copy[neighbor])

    return graph_copy[seat]

lily = Node("Lily Gladstone")
mark = Node("Mark Ruffalo")
cillian = Node("Cillian Murphy")
danielle = Node("Danielle Brooks")
lily.neighbors.extend([mark, danielle])
mark.neighbors.extend([lily, cillian])
cillian.neighbors.extend([danielle, mark])
danielle.neighbors.extend([lily, cillian])

copy = copy_seating(lily)
print(compare_graphs(lily, copy))

# TC: O(N + E) where N is the total Nodes / Vertices and E is the total directed edges.
# N (Total Nodes / Vertices):
#   - Queue Operations: Every reachable node enters q exactly once (when first discovered in the if neighbor not in
#   graph_copy: check) and is popped from q exactly once (q.popleft()).
#   - Each push and pop on a Python collections.deque is an O(1) operation.
#   - Node creation (Node(node.val, [])) and map lookups (node not in graph_copy) take O(1) amortized time.
#   - Contribution: O(N) operations across the entire execution.
# E (Total Directed Edges):
#   - The for loop iterations: When node is popped, we iterate through its adjacency list for neighbor in node.neighbors.
#   - Across the entire graph traversal, the inner loop executes once per outgoing edge.
#   - Inside the loop, checking map membership, creating missing clones, enqueuing, and list .append() operations are all O(1).
#   - Contribution O(E) work total across all nodes.
# SC: O(N) where N is the total Nodes / Vertices
#   - graph_copy map: Stores a mapping from every original node to its newly allocated clone. Requires O(N) space.
#   - q (BFS Queue): At peak execution, the queue holds at most the nodes on the frontier of the graph (maximum width), bounded by O(N).
#   - Auxiliary Space: O(N) extra memory (excluding the space required to store the cloned output graph structure itself, which takes O(N + E) space for nodes and edge references).

# Find Itinerary (Problem Set 1, Problem 8)

"""
Understand
1. What is the input structure?
2. What are the constraints and guarantees?
3. How do we identify the start node?

Plan
1. Check base edge case: If boarding_passes is empty, return [].
2. Initialize graph = {} for dep -> arr lookup and indegree = {} hash map to track incoming edges.
3. For each (dep, arr) pair in boarding_passes:
    a. Store graph[dep] = arr
    b. Ensure dep is indegree (initialize to 0 if not present).
    c. Increment indegree[arr] by 1 (indegree[arr] = indegree.get(arr, 0) + 1).
4. Find the starting airport:
    - Iterate through indegree.items() to locate the airport with degree == 0.
5. Reconstruct the itinerary:
    - Initialize itinerary = [start_airport] and curr = start_airport.
    - While curr exists in graph:
        i. Set curr = graph[curr]
        ii. Append curr to itinerary.
6. Return itinerary.
"""

# Implement
def find_itinerary(boarding_passes):
    if not boarding_passes:
        return []

    graph = {}
    indegree = {}

    for dep, arr in boarding_passes:
        graph[dep] = arr

        if dep not in indegree:
            indegree[dep] = 0
        indegree[arr] = indegree.get(arr, 0) + 1

    start_airport = None
    for airport, degree in indegree.items():
        if degree == 0:
            start_airport = airport
            break

    itinerary = [start_airport]
    curr = start_airport

    while curr in graph:
        curr = graph[curr]
        itinerary.append(curr)

    return itinerary

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))

# TC: O(V + E) where V is the total number of unique airports (vertices). Note that for a single linear path of length E, V = E + 1.
# E is the total number of boarding passes (edges). O(E) to populate the maps + O(V) to find the starting node + O(V) to traverse the chain.
# SC: O(V + E) where O(E) for graph + O(V) for the indegree hashmap and itinerary array.

# Secret Celebrity (Problem Set 2, Problem 5)

"""
Understand
1. What defines a Secret Celebrity (Town Judge)?
2. What if N = 1 and trust = []

Plan
1. Create a 2D array result of size N initialized to [0, 0]:
    - result[k][0] stores in-degree for person k + 1.
    - result[k][1] stores out-degree for person k + 1.
2. Iterate through each (i, j) pair in trust:
    - Increment result[j-1][0] (person j gains trust).
    - Increment result[i-1][1] (person i gives trust).
3. Loop through result from 0 to N-1:
    - If result[k][0] == N - 1 AND result[k][1] == 0:
        - Return k + 1.
4. Return -1 if no celebrity is found.
"""

# Implement
def identify_celebrity(trust, n):
    result = [[0, 0] for _ in range(n)]

    for i, j in trust:
        result[j-1][0] += 1
        result[i-1][1] += 1

    for i in range(n):
        if result[i][0] == n - 1 and result[i][1] == 0:
            return i + 1

    return -1

trust1 = [[1,2]]
trust2 = [[1,3],[2,3]]
trust3 = [[1,3],[2,3],[3,1]]

print(identify_celebrity(trust1, 2))
print(identify_celebrity(trust2, 3))
print(identify_celebrity(trust3, 3))

# TC: O(N + T) where N is the number of people and T is the number of trust relationships (edges in the graph).
#   - Initialization: Creating the array of size N takes O(N) time.
#   - Trust Traversal: Processing the T trust pairs takes O(T) time, doing O(1) updates per pair.
#   - Celebrity Lookup: Iterating through N entries takes O(N) time.
# SC: O(N)
#   - The auxiliary space is dominated by the result array (or scores array) storing degree metrics for N individuals.