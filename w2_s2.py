# Performer Schedule Pattern (Version 2, Problem 3)
"""
Understand
1. What if the key is empty?
2. Does the key contain all 26 lower case letters? if not what to do?

Plan
1. Initialize an empty dictionary mapping.
2. Loop through each char in key. If char is a letter and not already in mapping, assign
mapping[char] = chr(ord('a') + len(mapping)).
3. Loop through each char in message; retain ' ' as-is or replace
"""

# Implement
def decode_message(key: str, message: str) -> str:
    mapping = {}

    for char in key:
        if char.isalpha() and char not in mapping:
            mapping[char] = chr(ord('a')+len(mapping))

    decoded = []
    for char in message:
        if char == " ":
            decoded.append(" ")
        else:
            decoded.append(mapping[char])

    return "".join(decoded)

key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1))

key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "hntu depcte lxejw lxwntu zwx piqfx"

print(decode_message(key2, message2))

# TC: O(n+m) where n is the length of key and m is the length of message.
# SC: O(1), since the substitution dictionary stores at most 26 lowercase English letters.

# Longest Harmonious Travel Sequence (Version 2, Problem 4)
"""
Understand
1. What should the function return when the input array contains only identical elements (e.g., [1, 1, 1, 1]) and no rating + 1 pair exists?
2. Does the subsequence length represent the sum of occurrences of rating and rating + 1 (e.g., combining all instances of 2 and 3 if both are present)?

Plan
1. Fix dictionary initialization: Replace direct increment frequency[rating] += 1 with frequency[rating] = frequency.get(rating, 0) + 1 to prevent a KeyError on first encounter.
2. Fix adjacent lookup: Change frequency[rating] + frequency[rating - 1] to frequency[rating] + frequency[rating + 1] inside the condition if rating + 1 in frequency: to properly pair a rating with its +1 neighbor.
3. Track maximum length: Iterate through frequency, check for rating + 1 in frequency, and update max_length = max(max_length, frequency[rating] + frequency[rating + 1]) before returning max_length.
"""

# Implement
def find_longest_harmonious_travel_sequence(ratings):
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        frequency[rating] = frequency.get(rating, 0) + 1

    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length, frequency[rating] + frequency[rating + 1])

    return max_length

ratings1 = [1, 3, 2, 2, 5, 2, 3, 7]
ratings2 = [1, 2, 3, 4]
ratings3 = [1, 1, 1, 1]

print(find_longest_harmonious_travel_sequence(ratings1))  # 5
print(find_longest_harmonious_travel_sequence(ratings2))  # 2
print(find_longest_harmonious_travel_sequence(ratings3))  # 0

# Finding Common Tourist Attractions with Least Travel Time (Version 2, Problem 8)
"""
Understand
1. What should the function return if there are no common attractions between tourist_list1 and tourist_list2 (e.g., an empty list [] or None)?
2. If an attraction appears multiple times in either list, should we evaluate only its first appearance index or every occurrence? (Tip: storing the first occurrence in tourist_list1 is sufficient since a smaller index i will always yield a smaller sum i + j).

Plan
1. Build index map: Create a dictionary pos1 mapping each unique attraction in tourist_list1 to its first-seen index using enumerate(tourist_list1). (To optimize space, build the map from the shorter of the two lists).
2. Initialize tracking variables: Set min_sum = float('inf') and an empty list result = [].
3. Iterate and compare: Loop through tourist_list2 using enumerate(tourist_list2) to get index j and item.
4. Check intersection & sum: If item exists in pos1, compute current_sum = pos1[item] + j.
5. Update minimums & ties:
    - If current_sum < min_sum, update min_sum = current_sum and reassign result = [item].
    - If current_sum == min_sum, append item to result.
6. Return: Return result after completing the loop.
"""

def find_attractions(tourist_list1: list[str], tourist_list2: list[str]):
    pos1 = {item: idx for idx, item in enumerate(tourist_list1)}
    min_sum = float("inf")
    result = []

    for j, item in enumerate(tourist_list2):
        if item in pos1:
            current_sum = pos1[item] + j
            if current_sum < min_sum:
                min_sum = current_sum
                result = [item]
            elif current_sum == min_sum:
                result.append(item)

    return result

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Colosseum","Trevi Fountain","Pantheon","Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Disneyland","Eiffel Tower","Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach","mountain","forest"]
tourist_list2 = ["mountain","beach","forest"]

print(find_attractions(tourist_list1, tourist_list2))

# TC: O(N+M) where N and M are the lengths of tourist_list1 and tourist_list2. Building the hash map takes O(N) and scanning the second list takes O(M).
# SC: O(min(N, M)) to store the hash map for the smaller list, which is the theoretical lower bound for this problem.