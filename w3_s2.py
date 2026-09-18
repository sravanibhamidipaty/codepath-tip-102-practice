# Next Greater Event (Version 1, Problem 6)
"""
Understand
1. What should happen if an event in schedule1 has no greater event in schedule2?
2. Are the popularity scores in schedule2 guaranteed to be unique?

Plan
1. Get the lengths of schedule1 and schedule2, initialize result as an array of size len(schedule1) filled with -1, and
set up an empty stack and hash map schedule2_next_greater.
2. Iterate through each element in schedule2 using a monotonic decreasing stack:
    - While the stack is not empty and the current element is greater than stack[-1], pop the top of the stack and
    map the popped_element: current_element in schedule2_next_greater.
    - Push the current element onto the stack.
3. Iterate through schedule1 by index:
    - If schedule1[i] exists in schedule2_next_greater, update result[i] with the mapped value.
4. Return result.
"""

# Implement
def next_greater_event(schedule1: list[int], schedule2: list[int]): # [4, 1, 2], [1, 3, 4, 2]
    schedule1_length = len(schedule1)
    schedule2_length = len(schedule2)
    result = [-1] * schedule1_length
    stack = []
    schedule2_next_greater = {}

    for i in range(schedule2_length):
        while stack and schedule2[i] > stack[-1]:
            schedule2_next_greater[stack.pop()] = schedule2[i]
        stack.append(schedule2[i])

    for i in range(schedule1_length):
        if schedule1[i] in schedule2_next_greater:
            result[i] = schedule2_next_greater[schedule1[i]]

    return result


print(next_greater_event([4, 1, 2], [1, 3, 4, 2]))
print(next_greater_event([2, 4], [1, 2, 3, 4]))

# TC: O(n+m). Passing through schedule2 with a monotonic stack takes O(m) time because each element is pushed and popped at most once.
# Looking up each element of schedule1 in the hash map takes O(1) time, totaling O(n).
# SC: O(m). The stack and hash map schedule2_next_greater require O(m) space. This is auxiliary excluding the output result space.

# Final Costs After a Supply Discount (Version 2, Problem 1)
"""
Understand
1. What happens if a supply item has no subsequent item with a lesser or
equal cost (j > i with costs[j] <= costs[i])?
2. Which qualifying item provides the discount if multiple items to the right have a
cost less than or equal to costs[i]?

Plan
1. Create a copy of the input array (result = costs.copy()) to build and return the updated prices.
2. Initialize an empty stack to track indices of items that are still waiting to find a discounting item.
3. Iterate through costs using enumerate(costs):
    - While stack is not empty and the current cost is less than or equal to costs[stack[-1]]:
        - Pop the index idx from stack.
        - Subtract the discount: result[idx] = costs[idx] - cost.
    - Push the current index i onto stack.
4. Return result
"""

# Implement
def final_supply_costs(costs: list[int]): # [8, 4, 6, 2, 3]
    stack = []
    result = costs.copy()

    for i, cost in enumerate(costs):
        while stack and cost <= costs[stack[-1]]:
            index = stack.pop()
            result[index] = costs[index] - cost
        stack.append(i)

    return result

# TC: O(n) because each element is pushed and popped from the stack at most once.
# SC: O(n) for the stack and copy of the result array.

# Number of Explorers Unable to Gather Supplies (Version 2, Problem 5)
"""
Understand
1. Are explorers and supplies guaranteed to be the same length?
2. What stops the loop when remaining explores none want the top supply?

Plan
1. Count how many explorers prefer 0 and how many prefer 1 and store them in a hashmap.
2. Iterate through each resource s in supplies:
    - If there is at least one explorer who wants s (counts[s] > 0), decrement that count (counts[s] -= 1).
    - Otherwise, no one left in line can take this supply, so break out of the loop.
3. Return the sum of remaining counts sum(counts.values()) representing explorers who couldn't gather their supplies.
"""

# Implement
from collections import Counter

def count_explorers(explorers: list[int], supplies: list[int]):
    counts = Counter(explorers)

    for supply in supplies:
        if counts[supply] > 0:
            counts[supply] -= 1
        else:
            break

    return sum(counts.values())

# TC: O(n) to count preferences and single-pass the supplies array.
# SC: O(1) since preference types are restricted to just 0 and 1.