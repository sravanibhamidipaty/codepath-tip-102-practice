# Running Sum (Version 2, Problem 11)
"""
Understand
1. Can the superhero_stats have negative numbers? If so is that considered in the running sum?
2. Can the length of superheo_stats be 0 if so do I return the empty list or None?

Plan
Take the previous sum so far in the array and add the current number.
I need to modify the superhero_stats list itself because the question says to modify in place.
"""

# Implement
def running_sum(superhero_stats: list[int]) -> list[int]:
    n = len(superhero_stats)
    if n == 0 or n == 1:
        return superhero_stats

    for i in range(1, n):
        superhero_stats[i] += superhero_stats[i - 1]

    return superhero_stats


superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats))

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats))

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats))

# TC: O(n) where n is the number of elements in superhero_stats list.
# SC: O(1) since no additional data structures are used.

# Shuffle (Version 2, Problem 12)
"""
Understand
1. Can cards list be empty? If so do I return none?
2. The length says 2n does that mean the length of cards is always even?

Plan
Find the middle index based on the current cards length.
Create another empty list and have 2 pointers in the same direction to append the current value to the result.
"""

# Implement
def shuffle(cards: list[object]) -> list[object]:
    if len(cards) == 0:
        return []
    n = len(cards)
    mid = n // 2
    left = 0
    right = mid

    res = []

    while right < n:
        res.append(cards[left])
        res.append(cards[right])
        left += 1
        right += 1

    return res

cards = ["Joker", "Queen", 2, 3, "Ace", 7]
print(shuffle(cards))

cards = [9, 2, 3, "Joker", "Joker", 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))

# TC: O(n) where n is the number of elements in cards.
# SC: O(1) without including the result array.

# Tiggerfy (Version 1, Problem 11)
"""
Understand
1. If s is empty do I return an empty string?
2. If s doesn't have any tiger characters then do I return the string itself?

Plan
Have a set of tiger characters because sets have O(1) TC.
Then go through each character in s and then if it is not in the set then add it to a result list and return that list
after converting it to a string.
"""

# Implement
def tiggerfy(s: str) -> str:
    if len(s) == 0:
        return ""
    remove_characters = set("tiger")
    result = []

    for char in s:
        if char.lower() in remove_characters:
            continue
        else:
            result.append(char)

    return "".join(result)

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))

# TC: O(n) where n is the number of characters in s.
# SC: O(n) due to the result array.