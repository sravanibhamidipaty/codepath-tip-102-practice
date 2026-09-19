# Merging Missions (Problem Set 1, Problem 8)

"""
Understand
1. How should empty lists (None) be handled?
2. Should the merge be performed in-place or by creating new node objects?

Plan
1. Base Cases:
    - If mission1 is None, return mission2.
    - If mission2 is None, return mission1.
2. Recursive Step:
    - Compare mission1.value and mission2.value.
    - If mission1.value < mission2.value:
        - Set mission1.next = merge_missions(mission1.next, mission2).
        - Return mission1.
    - Else
        - Set mission2.next = merge_missions(mission1, mission2.next).
        - Return mission2.
"""

# Implement
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    if not mission1:
        return mission2
    if not mission2:
        return mission1

    if mission1.value < mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2

mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))

# TC: Each recursive call processes exactly 1 node by advancing either mission1 or mission2. In the worst case (where
# nodes alternate in value), the recursion continues until all nodes from both lists are evaluated. With n nodes in
# mission1 and m nodes in mission2, there are at most n + m recursive function calls. Since each call executes O(1)
# pointer operations, the total time complexity is O(n + m).
# SC: No new nodes are created in memory, so O(1) auxiliary memory is allocated on the heap.
# However, because each step makes a recursive call before returning, frames are added to the call stack.
# In the worst case, the recursion stack reaches a maximum depth of n + m. Therefore, the space complexity due to the
# call stack is O(n + m).

# Weaving Spells (Problem Set 2, Problem 8)

"""
Understand
1. What should happen if the two linked lists have different lengths?
2. Is the operation expected to be in-place?

Plan
1. Base Cases:
    - If spell_a is None, return spell_b.
    - If spell_b is None, return spell_a.
2. Recursive Step:
    - Connect spell_a.next to the result of calling weave_spells(spell_b, spell_a.next). (By passing spell_b first, 
    the next call attaches b_1, then a_2, then b_2, automatically creating the pattern).
3. Return Value:
    - Return spell_a as the current head.
"""

# Implement
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def weave_spells(spell_a, spell_b):
    if not spell_a:
        return spell_b
    if not spell_b:
        return spell_a
    spell_a.next = weave_spells(spell_b, spell_a.next)
    return spell_a

spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))

print_linked_list(weave_spells(spell_a, spell_b))

# TC: O(n + m), where n is the length of spell_a and m is the length of spell_b. Every node from both lists is visited
# once.
# SC: O(n + m) due to the recursive call stack depth.

# Finding the Longest Winning Streak (Problem Set 2, Problem 7)

"""
Understand
1. How should empty strings or strings without any 'S' be handled?
2. Can string slicing be used, or should an index parameter be passed?

Plan
1. Base Case:
    - If challenges is empty (""), return max_length.
2. Recursive Step: Look at the first character challenges[0]:
    - If challenges[0] == 'S':
        - Increment current_length by 1.
        - Update max_length = max(max_length, current_length).
    - Else
        - Reset current_length = 0.
3. Recurse: Call longest_streak(challenges[1:], current_length, max_length) on the remaining substring.
"""

# Implement
def longest_streak(challenges, current_length=0, max_length=0):
    if not challenges:
        return max_length

    if challenges[0] == 'S':
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0

    return longest_streak(challenges[1:], current_length, max_length)

print(longest_streak("SSOSSS"))
print(longest_streak("SOSOSOSO"))

# TC: O(n) recursive calls are made for a string of length n. Note that in Python, string slicing challenges[1:] takes
# O(k) time for a substring of length k, making the overall string-slicing execution O(n^2).
# If index-tracking is used instead of slicing, time complexity is pure O(n).
# SC: O(n) due to the maximum call stack depth reaching n frames before reaching the base case.