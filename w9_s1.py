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

# Icing Cupcakes in Zigzag Order (Problem Set 1, Problem 6)

"""
Understand
1. What should be returned if the input tree is empty (`cupcakes` is None)?
2. How does the traversal order alternate between levels?

Plan
1. Check for the edge case where cupcakes is None; if so, return [].
2. Initialize an empty list result to store the final list of flavors.
3. Initialize a queue using deque([cupcakes]) for level-order BFS traversal.
4. Set a boolean flag is_left = True to track direction for each level.
5. While queue is not empty:
   a. Capture the number of nodes at the current level: level_size = len(queue).
   b. Initialize a level deque: level_nodes = deque().
   c. Iterate level_size times:
      - Pop the front node from queue.
      - If is_left is True, append node.val to the right of level_nodes.
      - If is_left is False, prepend node.val to the left of level_nodes using appendleft().
      - Enqueue node.left and node.right if they exist.
   d. Extend result with level_nodes.
   e. Toggle is_left = not is_left for the next row.
6. Return result.
"""

# Implement
class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []

    result = []
    queue = deque([cupcakes])
    is_left = True

    while queue:
        level_size = len(queue)
        level_nodes = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if is_left:
                level_nodes.append(node.val)
            else:
                level_nodes.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(level_nodes)
        is_left = not is_left

    return result

flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))

# TC: O(N), where N is the total number of nodes in the binary tree. Each node is enqueued and dequeued exactly once.
# Inserting values into level_nodes using either append() or appendleft() on a Python deque takes O(1) amortized time
# per node, resulting in O(N) overall time.
# SC: O(N), where N is the total number of nodes in the binary tree. In a balanced or complete binary tree, the maximum
# number of nodes stored in the queue at any given time occurs at the lowest level, which holds up to N/2 nodes.
# Dropping constant factors, this simplifies to O(N).

# Mapping a Haunted Hotel (Problem Set 2, Problem 2)

"""
Understand
1. What should be returned if the tree is empty (`hotel` is None)?
2. In what order should the room values be returned?

Plan
1. Handle the base case: if hotel is None, return [].
2. Initialize an empty list rooms to store the output room values.
3. Initialize a queue using deque([hotel]) to process nodes level-by-level.
4. While queue is not empty:
   a. Pop the front node from queue using popleft().
   b. Append node.val to rooms.
   c. If node.left exists, append it to queue.
   d. If node.right exists, append it to queue.
5. Return rooms.
"""

# Implement
class Room:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def map_hotel(hotel):
    if not hotel:
        return []

    rooms = []
    q = deque([hotel])

    while q:
        node = q.popleft()
        rooms.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return rooms

hotel = Room("Lobby",
                Room(101, Room(201, Room(301)), Room(202)),
                Room(102, Room(203), Room(204, None, Room(302))))

print(map_hotel(hotel))

# TC: O(N), where N is the total number of rooms (nodes) in the hotel binary tree. Every room node in the binary tree is
# added to and removed from the double-ended queue exactly once. Each queue operation (popleft(), append()) takes O(1)
# constant time, giving an overall time complexity of O(N).
# SC: O(N), where N is the total number of rooms (nodes) in the hotel binary tree. The space complexity is determined
# by the maximum size of the queue during traversal, which occurs at the widest level of the binary tree. For a balanced
# binary tree, the leaf row contains up to N/2 nodes, which simplifies to O(N) in Big-O notation.

# Can Fulfill Order (Problem Set 1, Problem 5)

"""
Understand
1. What constitutes a valid path to fulfill the order?
2. What should be returned if inventory is empty (None)?

Plan
1. Check for the base edge case: if inventory is None, return False.
2. Initialize an explicit stack storing tuples of (node, current_sum): stack = [(inventory, inventory.val)].
3. While stack is not empty:
   a. Pop the top (node, current_sum) from stack.
   b. Check if node is a leaf (not node.left and not node.right):
      - If current_sum == order_size, return True.
   c. If node.right exists, push (node.right, current_sum + node.right.val) onto stack.
   d. If node.left exists, push (node.left, current_sum + node.left.val) onto stack.
4. If the loop completes without finding a matching leaf path sum, return False.
"""

# Implement
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def can_fulfill_order(inventory, order_size):
    if not inventory:
        return False

    stack = [(inventory, inventory.val)]

    while stack:
        node, current_sum = stack.pop()

        if not node.left and not node.right:
            if current_sum == order_size:
                return True

        if node.right:
            stack.append((node.right, current_sum+node.right.val))

        if node.left:
            stack.append((node.left, current_sum+node.left.val))

    return False

quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))

# TC: O(N), where N is the total number of nodes in the binary tree. In the worst case (when no path matches or the valid
# path is checked last), the algorithm visits each node in the tree at most once. Each stack push and pop operation takes O(1)
# constant time, resulting in an overall time complexity of O(N).
# SC: O(H), where H is the height of the tree.
#   - Balanced Tree: H = O(log N), so the stack holds at most O(log N) elements at any point.
#   - Skewed Tree (Worst Case): H = O(N), where the tree degenerates into a single line taking O(N) space.