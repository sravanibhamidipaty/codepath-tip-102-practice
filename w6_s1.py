# Magic Loop (Version 2, Problem 6)

"""
Understand
1. How do we know if a cycle exists before finding where it starts?
2. How do we find the exact node where the cycle begins once a meeting point is found?

Plan
1. Initialize slow and fast pointers to path_start and a boolean flag has_cycle = False.
2. Traverse the list using a while loop where fast moves 2 steps and slow moves 1 step.
3. If slow == fast, a cycle is detected: set has_cycle = True and break.
4. If the loop terminates without a match, return None (no cycle).
5. If a cycle exists, reset slow to path_start. Keep fast at the meeting point.
6. Advance both slow and fast one step at a time until they meet. The node where they meet is the start of the cycle; \
return its value.
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

def loop_start(path_start):
    slow = fast = path_start
    has_cycle = False

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    slow = path_start

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.value

path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1

print(loop_start(path_start))

# TC: O(N) where N is the total number of nodes in the linked list (both non-cyclic and cyclic parts).
# The first loop traverses the list to find the meeting point, and the second loop traverses from the head and the
# meeting point until they collide at the cycle start. Both phases scale linearly with the total number of nodes N.
# SC: O(1) because I only use a couple pointer variables (slow, fast, has_cycle) with no extra data structures.

# Mirror, Mirror (Version 2, Problem 5)

"""
Understand
1. How do we determine if a linked list reads the same forwards and backwards without using extra memory (like an array 
or stack)?
2. What happens if the list has an odd vs. even number of nodes?

Plan
1. Initialize slow and fast pointers at the head to find the middle of the linked list.
2. Reverse the second half of the linked list starting from the slow pointer using prev and curr pointers.
3. Compare the values of the nodes starting from the head (first half) and the prev pointer (reversed second half).
4. If any values don't match, return False. If we successfully check all nodes, return True.
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

def is_mirrored(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    while prev:
        if head.value != prev.value:
            return False
        head = head.next
        prev = prev.next

    return True

list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))

print(is_mirrored(list1))
print(is_mirrored(list2))

# TC: O(N) where N is the total number of nodes in the linked list.
# SC: O(1) because I am using pointers and no additional data structures.

# Volume Control (Version 1, Problem 6)

"""
Understand
1. What is a critical point?
2. Can the head or tail be critical points?
3. How do we check neighbors in a singly linked list?

Plan
1. If the list has fewer than 3 nodes, it's impossible to have a critical point, so return 0.
2. Initialize pointers and counter
3. Traverse the list
4. Check conditions for local maxima and minima
5. Advance pointers
6. Return counter
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

def count_critical_points(song_audio):
    if not song_audio or not song_audio.next or not song_audio.next.next:
        return 0

    count = 0
    prev = song_audio
    curr = song_audio.next

    while curr.next:
        next_node = curr.next
        if prev.value > curr.value and next_node.value > curr.value:
            count += 1
        elif prev.value < curr.value and next_node.value < curr.value:
            count += 1

        prev = curr
        curr = next_node

    return count

song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))

# TC: O(N) where N is the number of nodes in the linked list.
# SC: O(1) auxiliary space because we only use pointer variables (prev, curr, next_node) and a count integer.