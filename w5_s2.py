# Copy Linked List (Version 2, Problem 5)

"""
Understand
1. What makes a deep copy different from just copying the reference?
2. How do we keep track of the new list's head while building it?

Plan
1. Initialize a dummy node and a pointer curr2 starting at dummy, plus curr at the original head.
2. Traverse the original list with a while curr: loop.
3. Inside the loop, create a new Node(curr.value), attach it to curr2.next, and advance both pointers.
4. Return dummy.next as the head of the newly copied list.
"""

# Implement
class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def copy_ll(head):
    curr = head
    dummy = Node()
    curr2 = dummy
    while curr:
        curr2.next = Node(curr.value)
        curr = curr.next
        curr2 = curr2.next

    return dummy.next

mario = Node("Mario")
daisy = Node("Daisy")
luigi = Node("Luigi")
mario.next = daisy
daisy.next = luigi

# Linked List: Mario -> Daisy -> Luigi
copy = copy_ll(mario)

# Change original list -- should not affect the copy
mario.value = "Original Mario"

print_linked_list(mario)
print_linked_list(copy)

# TC: O(n) where n is the number of nodes in the linked list
# SC: O(n) where n is the number of nodes in the linked list

# Find Length of Doubly Linked List from Any Node (Version 2, Problem 10)

"""
Understand
1. What happens if you start at a node in the middle or end of a doubly linked list?
2. How do you find the true head of a doubly linked list from a random node?

Plan
1. Check the edge case: if the node is None, return 0.
2. Traverse backward using current = current.prev until you hit the true head.
3. Initialize a counter variable and traverse forward from the head using current = current.next, incrementing the 
counter at each node.
4. Return the final count.
"""

# Implement
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def get_length(node):
    if not node:
        return 0

    current = node
    while current.prev is not None:
        current = current.prev

    count = 0
    while current is not None:
        count += 1
        current = current.next

    return count

yoshi_falls = Node("Yoshi Falls")
moo_moo_farm = Node("Moo Moo Farm")
rainbow_road = Node("Rainbow Road")
dk_mountain = Node("DK Mountain")
yoshi_falls.next = moo_moo_farm
moo_moo_farm.next = rainbow_road
rainbow_road.next = dk_mountain
dk_mountain.prev = rainbow_road
rainbow_road.prev = moo_moo_farm
moo_moo_farm.prev = yoshi_falls

# List: Yoshi Falls <-> Moo Moo Farm <-> Rainbow Road <-> DK Mountain
print(get_length(rainbow_road))

# TC: O(n) where n is the number of nodes in the doubly linked list.
# SC: O(1) because there is only 2 pointers current and counter for state variables and no additional data structures are
# used.

# Move Tail to Front of Linked List (Version 1, Problem 8)

"""
Understand
1. What pointers do we need to adjust to move the tail to the front?
2. What if the linked list has 0 or 1 node?

Plan
1. Handle edge cases for an empty list or a single node list (return head).
2. Traverse the list until curr points to the second-to-last node (curr.next.next is None).
3. Extract the tail node (tail = curr.next) and detach it by setting curr.next = None.
4. Point the tail to the old head (tail.next = head).
5. Return the tail as the new head of the list.
"""

# Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def tail_to_head(head):
    if not head or not head.next:
        return head

    curr = head

    while curr.next.next is not None:
        curr = curr.next

    tail = curr.next
    curr.next = None
    tail.next = head
    return tail

daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad")
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

# Linked List: Daisy -> Mario -> Toad -> Peach
print_linked_list(tail_to_head(daisy))

# TC: O(n) where n is the number of nodes in the linked list
# SC: O(1) because no additional data structures are used