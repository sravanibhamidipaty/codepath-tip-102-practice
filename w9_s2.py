from collections import deque

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

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

# Transformable Bakery Orders (Problem Set 1, Problem 4)

"""
Understand
1. What are the base cases for comparing two nodes?
2. How can two non-null nodes with equal values match?

Plan
1. Check base cases:
   a. If not order1 and not order2, return True.
   b. If not order1 or not order2 or order1.val != order2.val, return False.
2. Recursively evaluate the two valid layout possibilities:
   a. no_swap: Check if left subtrees match left subtrees AND right subtrees match right subtrees.
   b. swap: Check if left subtree matches right subtree AND right subtree matches left subtree.
3. Return no_swap or swap.
"""

# Implement
class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def can_rearrange_orders(order1, order2):
    # Base Case 1: Both nodes are None
    if not order1 and not order2:
        return True

    # Base Case 2: One node is None or node values don't match
    if not order1 or not order2 or order1.val != order2.val:
        return False

    # Check without swapping left and right subtrees
    no_swap = can_rearrange_orders(
        order1.left, order2.left
    ) and can_rearrange_orders(order1.right, order2.right)

    # Check with swapping left and right subtrees
    swap = can_rearrange_orders(order1.left, order2.right) and can_rearrange_orders(
        order1.right, order2.left
    )

    return no_swap or swap

flavors1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot",
            None, None, None, None, "Chai", "Maple", None, "Smore"]
flavors2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]
order1 = build_tree(flavors1)
order2 = build_tree(flavors2)

print(can_rearrange_orders(order1, order2))

# TC: O(N) where N is the total number of nodes in order1 and order2. At each node, short-circuit evaluation prevents
# unnecessary recursive paths once a match failure occurs. Because each node has unique values or bounded recursive
# branch evaluations, we visit each corresponding node pair at most a constant number of times, resulting in O(N)
# overall time.
# SC: O(H) where H is the height of the binary trees. Space is determined by the maximum depth of the call stack during
# the recursive DFS traversal:
#   - Balanced Tree: H = O(log N), so the recursion stack requires O(log N) memory.
#   - Skewed Tree (Worst Case): H = O(N), where the tree degrades into a single line, taking O(N) memory.

# Larger Order Tree (Problem Set 1, Problem 5)

"""
Understand
1. How do we convert recursive reverse in-order traversal to iterative?
2. How do we update node values?

Plan
1. Initialize running_sum = 0, an empty list stack = [] and curr = root.
2. Loop while curr is not None or stack is not empty:
    a. Push curr and all of its right descendants onto stack: curr = curr.right.
    b. Pop the top node from stack: curr = stack.pop()
    c. Update running_sum += curr.val
    d. Assign curr.val = running_sum.
    e. Move to the left child: curr = curr.left
3. Return root.
"""

# Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def larger_order_tree(orders):
    running_sum = 0
    stack = []
    curr = orders

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.right

        curr = stack.pop()
        running_sum += curr.val
        curr.val = running_sum

        curr = curr.left

    return orders

# TC: O(N) where N is the total number of nodes in the BST. Each node is pushed to and popped from the stack exactly once.
# SC: O(H), where H is the height of the tree. The stack stores nodes along a single path from root to leaf.
#   - Balanced BST: H = O(log N)
#   - Skewed BST (Worst Case): H = O(N)

# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))

# Sectioning Off Cursed Zones (Problem Set 2, Problem 6)

"""
Understand
1. What defines the "deepest rooms"?
2. What if there is only one deepest room?
3. What if there are multiple deepest rooms?

Plan
1. Use a post-order Depth-First Search (DFS) bottom-up approach returning a tuple (depth, lca_node) for each subtree:
    - depth: Maximum depth of any room in the subtree rooted at node.
    - lca_node: Root of the smallest subtree containing all deepest rooms within that subtree.
2. Base Case:
    - If node is None, return depth 0 and None.
3. Recursive Steps:
    - Recurse on left child: left_depth, left_lca = dfs(node.left)
    - Recurse on right child: right_depth, right_lca = dfs(node.right)
4. Merge Results:
    - If left_depth == right_depth: The deepest rooms are split equally across left and right subtrees. Therefore, the
    current node is the lowest common ancestor for all deepest rooms beneath it. Return (left_depth+1, node).
    - If left_depth > right_depth: All deepest rooms lie strictly in the left subtree. Return (left_depth+1, left_lca).
    - If right_depth > left_depth: All deepest rooms lie strictly in the right subtree. Return (right_depth+1, right_lca).
5. Execute dfs(hotel) and return the second element of the returned tuple (lca_node).
"""

# Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def smallest_subtree_with_deepest_rooms(hotel):
    def dfs(node):
        if not node:
            return 0, None

        left_depth, left_lca = dfs(node.left)
        right_depth, right_lca = dfs(node.right)

        if left_depth == right_depth:
            return left_depth + 1, node

        if left_depth > right_depth:
            return left_depth + 1, left_lca

        return right_depth + 1, right_lca

    return dfs(hotel)[1]

rooms = ["Lobby", 101, 102, 201, 202, 203, 204, None, None, "😱", "👻"]
hotel1 = build_tree(rooms)
rooms = ["Lobby", 101, 102, None, "💀"]
hotel2 = build_tree(rooms)

# Using print_tree() function included at top of page
print_tree(smallest_subtree_with_deepest_rooms(hotel1))
print_tree(smallest_subtree_with_deepest_rooms(hotel2))

# TC: O(N), where N is the total number of nodes (rooms) in the hotel binary tree. The post-order DFS traversal visits
# every node in the binary tree exactly once. At each node, the algorithm performs O(1) constant time operations
# (integer comparisons, addition, and tuple packing). Thus, total running time scales linearly with the total number of
# nodes N, resulting in an overall time complexity of O(N).
# SC: O(H), where H is the height of the hotel binary tree. The auxiliary space footprint is determined exclusively by
# the maximum depth of the call stack during recursive DFS traversal:
#   - Balanced Tree: H = O(log N), so at most O(log N) stack frames are stored simultaneously.
#   - Skewed Tree (Worst Case): H = O(N), where the binary tree degenerates into a single path, requiring O(N) stack frames.