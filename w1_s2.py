# Exposing Superman (Version 2, Problem 10)
"""
Understand
1. What to return if trust is empty?
2. Can there be random trust connections where n is invalid?

Plan
1. Create an array of size n+1
2. Add in degrees to the array of who is being trusted. Also create a graph for how many people the current person
is trusting.
3. Go through the array from range 1 to n and then figure out where count = n-1. If it is check the dictionary
of how many people this person is trusting. If they trust none then return this person or return -1 at the end
"""

# Implement
def expose_superman(trust: list[list[int]], n: int) -> int:
    trusts_count = {i:0 for i in range(1, n+1)}
    trusted = [0] * (n+1)

    for a, b in trust:
        trusted[b] += 1
        trusts_count[a] += 1

    for i in range(1, n+1):
        if trusted[i] == n-1:
            if trusts_count[i] == 0:
                return i

    return -1

# TC: O(N+E) where n is the number of people and E is the number of edges
# SC: O(N) because I am creating a dictionary with n people and an array with n people so the big bucket is O(n)

n = 2
trust = [[1, 2]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n))

# Eeyore's House (Version 1, Problem 10)
"""
Understand
1. Can one of the arrays be none or both are none if one is none? If so what to return?
2. Can the pairs have negative numbers? What is an example of what that returns?

Plan
Nested for loops going acorss nums1 and nums2 and figuring out with an if statement if the given modulus condition
is true, count += 1 and then return the count.
"""

# Implement
def good_pairs(pile1: list[int], pile2: list[int], k: int) -> int:
    counter = 0
    for num1 in pile1:
        for num2 in pile2:
            if num1 % (num2 * k) == 0:
                counter += 1

    return counter

# TC: O(n*m) where n is the length of pile1 and m is the length of pile2.
# SC: O(1) since there are no additional data structures used.

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))

# Left and Right Sum Differences (Version 2, Problem 8)
"""
Understand
1. Can the numbers be negative? If so 1 + -1 will sum for example be 0?
2. Can the array be empty? If so do I return None or an empty array?

Plan
sum all the numbers. build up a current sum starting at 0. left sum is the current sum and right sum is the total
minus the current sum and add that to the answer
"""
def left_right_difference(nums: list[int]) -> list[int]:
    current_sum = 0
    total_sum = sum(nums)
    answer = []

    for num in nums:
        total_sum -= num
        answer.append(current_sum-total_sum)
        current_sum += num

    return answer

# TC: O(n) where n is the length of the array
# SC: O(1) auxiliary without including the output array

nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))