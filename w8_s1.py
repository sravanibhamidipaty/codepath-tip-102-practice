# Ocean Layers (Problem Set 2, Problem 7)

"""
Understand
1. What should be returned if the tree is empty (root is None)?
2. How is tree depth defined?

Plan
1. Guard Clause: If root is None, return 0.
2. Initialize Stack & Max Depth:
    - Create a stack with the tuple (root, 1) representing (node, current_depth).
    - Initialize max_depth = 0.
3. Iterative DFS Traversal:
    - While stack is not empty:
        - Pop (node, depth) from the stack.
        - Update max_depth = max(max_depth, depth).
        - If node.right exists, push (node.right, depth + 1) onto the stack.
        - If node.left exists, push (node.left, depth + 1) onto the stack.
4. Return max_depth.
"""

# Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def ocean_depth(root):
    if not root:
        return 0

    stack = [(root, 1)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth+1))

    return max_depth

ocean = TreeNode("Sunlight",
                TreeNode("Twilight",
                        TreeNode("Abyss",
                                TreeNode("Trenches")), TreeNode("Anglerfish")),
                                        TreeNode("Squid", TreeNode("Giant Squid")))

tidal_zones = TreeNode("Spray Zone",
                      TreeNode("Beach"),
                              TreeNode("High Tide",
                                      TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))
print(ocean_depth(tidal_zones))

# TC: O(n), where n is the total number of nodes in the binary tree. Every node is visited exactly once.
# SC: O(h), where h is the height of the binary tree, due to the memory used by the stack frame.
# - Worst case: O(n) for a completely skewed tree.
# - Best/Average case: O(log n) for a balanced binary tree.

# Foraging Berries (Problem Set 1, Problem 7)

"""
Understand
1. What should be returned if the tree is empty (root is None)?
2. What condition determines if berries on a node should be harvested?

Plan
1. Guard Clause: If root is None, return 0.
2. Initialize State:
    - Set total_sum = 0.
    - Create a stack initialized with [root].
3. Iterative DFS Traversal:
    - While stack is not empty:
        - Pop node from stack.
        - If node.val > threshold, add node.val to total_sum.
        - If node.right exists, push node.right onto stack.
        - If node.left exists, push node.left onto stack.
4. Return total_sum.
"""

# Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvest_berries(root, threshold):
    if not root:
        return 0

    total_sum = 0
    stack = [(root)]

    while stack:
        node = stack.pop()
        if node.val > threshold:
            total_sum += node.val

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return total_sum

bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvest_berries(bush, 6))
print(harvest_berries(bush, 30))

# TC: O(n) where n is the total number of nodes in the binary tree. Every node is visited exactly once.
# SC: O(h) where h is the height of the binary tree, due to the memory used by the stack frame.
#   - Worst case: O(n) for a completely skewed tree.
#   - Best/Average case: O(log n) for a balanced binary tree.

# Flower Fields (Problem Set 1, Problem 8)

"""
Understand
1. What should be returned if the tree is empty (root is None)?
2. Is the tree a Binary Search Tree (BST) or an unsorted Binary Tree?

Plan
1. Guard Clause: If root is None, return False.
2. Initialize Stack: Create a stack initialized with [root].
3. Iterative DFS Traversal:
    - While stack is not empty:
        - Pop the current node from the stack.
        - If node.val == flower:
            - Found target flower; return True.
        - If node.right exists, push node.right onto the stack.
        - If node.left exists, push node.left onto the stack.
4. If the traversal completes without finding flower, return False.
"""

# Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(root, flower):
    if not root:
        return False

    stack = [root]

    while stack:
        node = stack.pop()

        if node.val == flower:
            return True

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return False

# TC: O(n) where n is the total number of nodes in the binary tree. Every node is visited exactly once.
# SC: O(h) where h is the height of the binary tree, due to the memory used by the stack frame.
#   - Worst case: O(n) for a completely skewed tree.
#   - Best/Average case: O(log n) for a balanced binary tree.