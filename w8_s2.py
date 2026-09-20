from collections import deque
def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Remove Plant (Problem Set 1, Problem 7)

"""
Understand
1. What should be returned if name is not found in the tree or if collection is empty?
2. How is a node with two children removed according to the problem prompt?

Plan
1. Base Case: If collection is None, return None.
2. Search Phase (Navigate BST):
    - If name < collection.val, recursively search/update left: collection.left = remove_plant(collection.left, name).
    - Elif name > collection.val, recursively search/update right: collection.right = remove_plant(collection.right, name).
3. Deletion Phase (Found target node where collection.val == name):
    - Case 1 & 2 (0 or 1 child):
        - If collection.left is None, return collection.right.
        - Elif collection.right is None, return collection.left.
    - Case 3 (2 children):
        - Find the inorder predecessor: set pred = collection.left, then iterate while pred.right: pred = pred.right.
        - Overwrite current node's value: collection.val = pred.val.
        - Recursively delete the predecessor node: collection.left = remove_plant(collection.left, pred.val).
4. Return collection as the root of the modified subtree.
"""

# Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    if not collection:
        return None

    # Step 1: Search for the node to remove
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        # Found the node! Handle the 3 deletion cases:

        # Case 1 & 2: Node has 0 or 1 child
        if not collection.left:
            return collection.right
        elif not collection.right:
            return collection.left

        # Case 3: Node has 2 children
        # 1. Find inorder predecessor (rightmost node in left subtree)
        pred = collection.left
        while pred.right:
            pred = pred.right

        # 2. Replace current node's value with predecessor's value
        collection.val = pred.val

        # 3. Recursively remove the predecessor node from the left subtree
        collection.left = remove_plant(collection.left, pred.val)

    return collection

values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))

# TC: O(h), where h is the height of the tree. Assuming the tree is balanced as stated in the problem, h = log n,
# making the time complexity O(log n). In the worst case (a skewed tree), it would be O(n).
# SC: O(h) (or O(log n) for a balanced tree) due to the recursive call stack.

# Finding a New Plant Within Budget (Problem Set 1, Problem 6)

"""
Understand
1. What should be returned if no plant has a price strictly below budget or if inventory is empty?
2. How are the TreeNode attributes mapped?
3. Is a plant price equal to budget valid?

Plan
1. Initialize best_plant = None to track the name of the highest-priced valid plant found.
2. Initialize pointer curr = inventory to traverse the BST.
3. Iterative BST Search Loop (while curr is not None):
    - If curr.key >= budget:
        - Current price is too high or equal to budget. Search the left subtree for lower prices: curr = curr.left.
    - Else (curr.key < budget):
        - Current plant is strictly below budget! Save its name: best_plant = curr.val.
        - Try to find a higher valid price by searching the right subtree: curr = curr.right.
4. Return best_plant.
"""

# Implement
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right



def pick_plant(inventory, budget):
    best_plant = None
    curr = inventory

    while curr:
        if curr.val >= budget:
            curr = curr.left
        else:
            best_plant = curr.key
            curr = curr.right

    return best_plant

values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"),
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

print(pick_plant(inventory, 50))
print(pick_plant(inventory, 25))
print(pick_plant(inventory, 15))

# TC: O(h), where h is the height of the binary search tree.
#     - Best/Average Case (balanced tree): O(log n), where n is the total number of nodes.
#     - Worst Case (skewed tree): O(n).
# Rationale: In each step of the loop, we descend one level down the tree (moving either left or right) without backtracking.
# SC: O(1) auxiliary space because we use an iterative while loop with a single pointer (curr) and tracking variable
# (best_plant) without extra data structures or recursive call stack space

# Minimum Difference in Pearl Sizes (Problem Set 2, Problem 7)

"""
Understand
1. What if the tree has fewer than 2 pearls?
2. Are negative values or duplicates possible?

Plan
1. Initialize Traversal State:
    - Set stack = [] and curr = pearls.
    - Set prev_val = None to keep track of the previously visited pearl's size.
    - Set min_diff = float('inf') to record the smallest difference.
2. Iterative Inorder Traversal (Left -> Node -> Right):
    - While curr is not None or stack is not empty:
        - Reach the leftmost node: while curr is not None, push curr onto stack and set curr = curr.left.
        - Pop node from stack: curr = stack.pop().
        - Process Node:
            - If prev_val is not None, update min_diff = min(min_diff, curr.val - prev_val).
            - Set prev_val = curr.val.
        - Move to right subtree: curr = curr.right.
3. Return min_diff.
"""

# Implement
class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(pearls):
    if not pearls:
        return 0

    stack = []

    curr = pearls

    prev_val = None
    min_diff = float("inf")

    while curr or stack:
        # Traverse to leftmost node
        while curr:
            stack.append(curr)
            curr = curr.left

        # Visit node
        curr = stack.pop()

        if prev_val is not None:
            min_diff = min(min_diff, curr.val - prev_val)
        prev_val = curr.val

        # Traverse right subtree
        curr = curr.right

    return min_diff

values = [4, 2, 6, 1, 3, None, 8]
pearls = build_tree(values)

print(min_diff_in_pearl_sizes(pearls))
# TC: O(n), where n is the total number of pearls/nodes in the BST. Every node is visited exactly once during the inorder traversal.
# SC: O(h), where h is the height of the BST, due to the call stack size.
#   - Best/Average Case (balanced tree): O(\log n)
#   - Worst Case (skewed tree): O(n)