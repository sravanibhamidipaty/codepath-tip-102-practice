def print_linked_list(head):
    current = head
    if not head:
        print("Empty List")
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Split Linked List in Parts (Problem Set 2, Problem 6)

"""
Understand
1. How do we distribute N nodes across k parts evenly?
2. What if the list has fewer nodes than k (N < k)?
3. How do we disconnect each part?

Plan
1. Count total nodes (N): Traverse the linked list once to find its total length.
2. Calculate part sizes: Compute base_size = N // K and extra N % k.
3. Initialize result list: Create an array parts of size k initializes with None.
4. Iterate and disconnect:
    - Loop i from 0 to k - 1.
    - If curr is None, stop early (the remaining parts in parts stay None).
    - Set parts[i] = curr.
    - Compute part_size = base_size + (1 if i < extra else 0).
    - Traverse part_size - 1 steps to reach the tail node of the current part.
    - Save next_node = curr.next, set curr.next = None to disconnect, and advance curr = next_node.
5. Return parts.
"""

# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def split_list(head, k):
    # Step 1: Calculate total length of the linked list
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    # Step 2: Determine base size and extra nodes
    base_size = length // k
    extra = length % k

    parts = [None] * k
    curr = head

    # Step 3: Split into k parts
    for i in range(k):
        if not curr:
            break

        parts[i] = curr
        # The first `extra` parts get 1 additional node
        part_size = base_size + (1 if i < extra else 0)

        # Traverse to the last node of the current part
        for _ in range(part_size - 1):
            curr = curr.next

        # Disconnect the current part from the rest of the list
        next_node = curr.next
        curr.next = None
        curr = next_node

    return parts

list_1 = Node(1, Node(2, Node(3)))
list_1_output = split_list(list_1, 5)

for part in list_1_output:
    print_linked_list(part)

list_2 = Node(1, Node(2, Node(3, Node(4, Node(5,
                Node(6, Node(7, Node(8, Node(9, Node(10))))))))))
list_2_output = split_list(list_2, 3)

for part in list_2_output:
    print_linked_list(part)

# TC: O(N + k) where N is the number of nodes in the linked list.
#   - Constructing the nodes takes O(N) time.
#   - Constructing the k parts traverses through each node in the list once, taking O(N) time, plus O(k) time to allocate and populate the result array of size k.
# SC: O(1) auxiliary space (or O(k)) to store the output array.
#   - Nodes are disconnected in-place without allocating new nodes or deep copies.

# Find All Paths From Source to Target (Problem Set 1, Problem 6)

"""
Understand
1. What is the start and end point?
2. Can a node be part of multiple paths?

Plan
1. Determine target = len(graph) - 1.
2. Initialize stack = [(0, [0])] and an empty list result = [].
3. While stack is not empty:
    - Pop (node, path).
    - If node == target, append path to result.
    - Otherwise, for each neighbor in graph[node]:
        - Push (neighbor, path + [neighbor]) onto stack.
4. Return result.
"""

# Implement
def all_paths(graph):
    target = len(graph) - 1
    result = []
    stack = [(0, [0])]

    while stack:
        node, path = stack.pop()

        if node == target:
            result.append(path)
            continue

        for neighbor in graph[node]:
            stack.append((neighbor, path + [neighbor]))

    return result

graph_1 = [[1,2],[3],[3],[]]
print(all_paths(graph_1))

graph_2 = [[4,3,1],[3,2,4],[3],[4],[]]
print(all_paths(graph_2))

# Why are there 2^(V-2) total paths?
#   - Node 0 is always at the start.
#   - Node V - 1 is always at the end.
#   - Every intermediate node in {1, 2, ..., V-2} can either be included or excluded from the path.
#   - Since there are V - 2 intermediate nodes and each has 2 choices (in or out), the total number of distinct paths is: 2^(V-2) = O(2^(V))
# TC: O(V x 2^V). The time complexity comes down to two factors: number of paths x work done per path.
#   - Number of Paths: There are O(2^V) distinct paths from source to target in the worst case.
#   - Work Per Path:
#       - When building path arrays in Python using path + [neighbor], copying an array of length L takes O(L) time.
#       - Since a path can be up to V nodes long, building and appending each complete path takes O(V) time.
# SC: O(V)
#   - For stack depth: At most V frames.
#   - Path tracker: At most V nodes stored.
#   - Auxiliary Space excluding the final result array.

# Number of Provinces (Problem Set 2, Problem 5)

"""
Understand
1. What does is_connected represent?
2. What is a province?

Plan
1. Let n = len(is_connected).
2. Initialize parent = [0, 1, ..., n-1]
3. Define find(i) with path compression to locate the root representative of city i.
4. Define union(i, j) with union by rank:
    - Find roots root_i = find(i) and root_j = find(j).
    - If root_i != root_j, attach one tree under another, update ranks, and decrement provinces -= 1.
5. Iterate through the upper triangle of is_connected (i form 0 to n-1, j from i+1 to n-1):
    - If is_connected[i][j] == 1, call union(i, j).
6. Return provinces.
"""

# Implement
def num_provinces(is_connected):
    n = len(is_connected)
    parent = [i for i in range(n)]
    rank = [1] * n
    provinces = n

    def find(i):
        while i != parent[i]:
            parent[i] = parent[parent[i]]
            i = parent[i]

        return i

    def union(i, j):
        nonlocal provinces
        root_i = find(i)
        root_j = find(j)

        if root_i == root_j:
            return

        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
        elif rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_j] = root_i
            rank[root_i] += 1

        # Successful merge reduces total disjoint components by 1
        provinces -= 1

    for i in range(n):
        for j in range(i+1, n):
            if is_connected[i][j] == 1:
                union(i, j)

    return provinces

is_connected_1 = [[1,1,0],[1,1,0],[0,0,1]]
print(num_provinces(is_connected_1))

is_connected_2 = [[1,0,0],[0,1,0],[0,0,1]]
print(num_provinces(is_connected_2))

# TC: O(N^2 x alpha(N))
#   - We iterate over all O(N^2) entries in the adjacency matrix.
#   - Each find and union operation takes O(alpha(N)) time, where alpha is the inverse Ackermann function. Since alpha(N) <= 4 for all practical inputs, it is practically O(1) constant time.
# SC: O(N)
#   - Requires O(N) auxiliary space for the parent array and rank array of size N.
#   - Iterative path halving uses O(1) auxiliary stack space (no recursion call stack).