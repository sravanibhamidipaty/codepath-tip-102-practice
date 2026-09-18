# Adding Up the Evidence (Version 1, Problem 6)

"""
Understand
1. How are the numbers represented in the linked lists?
2. How do we handle unequal list lengths and leftover carries?

Plan
1. Initialize a dummy result node, a pointer `curr` starting at the dummy, and a `carry` variable set to 0.
2. Create a `while` loop that runs while `head_a`, `head_b`, or `carry` is truthy.
3. Inside the loop, start `total` with the value of `carry`. Add `head_a.value` if `head_a` exists, then advance
`head_a`. Do the same for `head_b`.
4. Create a new node with the digit `total % 10`, attach it to `curr.next`, and advance `curr`.
5. Update `carry` to `total // 10` for the next iteration.
6. Return `result.next` as the head of the new sum linked list.
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

def add_two_numbers(head_a, head_b):
    if not head_a and not head_b:
        return head_a
    if head_a and not head_b:
        return head_a
    if head_b and not head_a:
        return head_b
    result = Node(-1)
    curr = result
    total = 0
    carry = 0

    while head_a or head_b or carry:
        total = carry

        if head_a:
            total += head_a.value
            head_a = head_a.next

        if head_b:
            total += head_b.value
            head_b = head_b.next

        curr.next = Node(total%10)
        curr = curr.next
        carry = total//10

    curr.next = head_a or head_b
    return result.next

head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))

# TC: O(n + m) where n and m are the lengths of head_a and head_b, as we iterate through both lists.
# SC: O(max(n, m)) auxiliary space for the newly generated output linked list (plus at most 1 node for a final carry).

# Controlled Burns (Version 2, Problem 4)

"""
Understand
1. How do we process the linked list in segments of keeping and deleting?
2. How do we safely bridge the gap after deleting n nodes?

Plan
1. Handle edge cases: if the list is empty, return the head as-is.
2. Initialize a traversal pointer (`curr = trailhead`) and loop while `curr` exists.
3. Advance `curr` through the keep-zone by moving $m - 1$ steps forward.
4. Set up a pointer (`temp = curr.next`) and loop $n$ times to find the safe landing node past the delete-zone.
5. Rewire the connection by setting `curr.next = temp` to drop the skipped nodes.
6. Advance `curr = temp` to reset for the next keep/delete cycle and return the modified `trailhead`.
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

def selective_trail_clearing(trailhead, m, n):
    if not trailhead:
        return trailhead

    curr = trailhead

    while curr:
        for _ in range(m - 1):
            if not curr.next:
                break
            curr = curr.next

        temp = curr.next
        for _ in range(n):
            if not temp:
                break
            temp = temp.next

        curr.next = temp
        curr = temp

    return trailhead

trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))

print_linked_list(selective_trail_clearing(trailhead, 2, 3))

# TC: O(N). Where N is the total number of nodes in the linked list. Even though we have nested loops, every single node
# is visited and processed at most once as your pointers move forward through the keep-and-skip cycles.
# SC: O(1). The list is modified completely in-place by rewiring existing node pointers (curr and temp).
# No additional data structures (like arrays, stacks, or new nodes) are allocated that scale with the size of the
# input list.

# Removing Duplicate Markers (Version 2, Problem 3)

"""
Understand
1. What do we need to do with nodes that have duplicate values?
2. Why do we need a dummy head node?

Plan
1. Create a dummy node with a placeholder value and set `dummy.next = trailhead`.
2. Initialize a pointer `curr = dummy` to keep track of our position.
3. Traverse the list using a `while` loop that checks `curr.next and curr.next.next`.
4. If a duplicate pair is found (`curr.next.value == curr.next.next.value`), save that value 
   in `duplicate_value`.
5. Use an inner `while` loop to skip and delete *all* consecutive nodes matching `duplicate_value`.
6. If no duplicate is found, advance `curr = curr.next` normally.
7. Return `dummy.next` as the head of the modified list.
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

def remove_duplicate_markers(trailhead):
    dummy = Node(-1)
    dummy.next = trailhead
    curr = dummy

    while curr.next and curr.next.next:
        if curr.next.value == curr.next.next.value:
            duplicate_value = curr.next.value
            while curr.next and curr.next.value == duplicate_value:
                curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next

trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))

print_linked_list(remove_duplicate_markers(trailhead))

# TC: O(N) where N is the number of nodes in the linked list. Every node is visited at most a constant number of times
# across the outer and inner loops.
# SC: O(1) auxiliary space because we modify the list completely in-place using pointers and a single duplicate value
# tracker variable.