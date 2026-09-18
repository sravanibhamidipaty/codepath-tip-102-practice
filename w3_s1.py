# Post Compare (Version 1, Problem 7)
"""
Understand
1. What if one draft string is empty or results in an empty string after backspaces?
2. How do consecutive '#' characters affect the preceding characters?

Plan
1. Use two pointers starting from the end of both strings (draft1_ptr, draft2_ptr).
2. Use skip counters (skip1, skip2) to track how many characters need to be deleted when encountering '#'.
3. Traverse both strings backward, skipping characters marked by backspaces.
4. Compare the valid characters; if they mismatch or one string runs out before the other, return False.
"""

# Implement
def post_compare(draft1: str, draft2: str) -> bool:
    draft1_length = len(draft1)
    draft2_length = len(draft2)
    draft1_ptr = draft1_length - 1
    draft2_ptr = draft2_length - 1
    skip_draft1 = 0
    skip_draft2 = 0

    while draft1_ptr >= 0 or draft2_ptr >= 0:
        while draft1_ptr >= 0:
            if draft1[draft1_ptr] == "#":
                skip_draft1 += 1
                draft1_ptr -= 1
            elif skip_draft1 > 0:
                skip_draft1 -= 1
                draft1_ptr -= 1
            else:
                break

        while draft2_ptr >= 0:
            if draft2[draft2_ptr] == "#":
                skip_draft2 += 1
                draft2_ptr -= 1
            elif skip_draft2 > 0:
                skip_draft2 -= 1
                draft2_ptr -= 1
            else:
                break

        if draft1_ptr >= 0 and draft2_ptr >= 0:
            if draft1[draft1_ptr] != draft2[draft2_ptr]:
                return False
        elif draft1_ptr >= 0 or draft2_ptr >= 0:
            return False

        draft1_ptr -= 1
        draft2_ptr -= 1
    return True

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#"))
print(post_compare("a#c", "b"))

# TC: O(n+m) because each character in draft1 (of length n) and each character in draft2 (of length m) is visited at most once by its respective pointer, making the total work proportional to the combined length of both strings.
# SC: O(1) because only a fixed number of variables are used regardless of the input sizes, with no auxiliary data structures or string reconstruction required.

# Minimum Remaining Watchlist After Removing Movies (Version 2, Problem 5)
"""
Understand
1. What should happen if the input watchlist is empty ("")?
2. How are cascading/chain-reaction pairs handled when remove "AB" or "CD" exposes new adjacent pairs?

Plan
1. Initialize an empty list stack to keep track of characters.
2. Iterate through each char in watchlist.
3. Check if stack is non-empty and if (stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D').
    - If true, call stack.pop() to remove the matched pair.
    - If false, call stack.append(char) to push the current character.
4. Return len(stack) as the minimum possible length of the remaining watchlist.
"""

# Implement
def min_remaining_watchlist(watchlist: str) -> int:
    stack = []
    for i, char in enumerate(watchlist):
        if stack and (stack[-1] == "A" and char == "B" or stack[-1] == "C" and char == "D"):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)

print(min_remaining_watchlist("ABFCACDB"))
print(min_remaining_watchlist("ACBBD"))

# TC: O(n). You iterate through the string of length n a single time, and every push or pop operation on the stack is O(1).
# You cannot achieve better than O(n) time because you must inspect every character in the input at least once.
# SC: O(n). In the worst-case scenario (where no pairs can be removed), the stack stores all n characters.

# Lexicographically Smallest Watchlist (Version 2, Problem 7)
"""
Understand
1. What should happen if the string is already a palindrome or has an odd/even length?
2. When a character mismatch occurs between watchlist[left] and watchlist[right], which character should be replaced to make the 
result lexographically smallest?

Plan
1. Convert the input string watchlist into a mutable list of characters (lst = list(watchlist)).
2. Initialize two pointers: left = 0 at teh start and right = len(lst) - 1 at the end.
3. Loop while left < right:
    - Compare lst[left] and lst[right].
    - If they are different, update both lst[left] and lst[right] to min(lst[left], lst[right]).
    - Move left one step right (left += 1) and right one step left (right -= 1).
4. Join the list back into a string ("".join(lst)) and return it.
"""

# Implement
def make_smallest_watchlist(watchlist):
    # 1. Convert the watchlist string to a list
    lst = list(watchlist)

    # 2. Initialize two pointers
    left = 0
    right = len(lst) - 1

    # 3. While the left pointer is less than the right pointer
    while left < right:
        # a. Compare characters at left and right pointers
        if lst[left] != lst[right]:
            # b. Replace the larger (alphabetically later) character with the smaller one
            smaller_char = min(lst[left], lst[right])
            lst[left] = smaller_char
            lst[right] = smaller_char

        # c & d. Move pointers inward
        left += 1
        right -= 1

    # 4. Convert list back to string and 5. Return the resulting string
    return "".join(lst)

print(make_smallest_watchlist("egcfe"))
print(make_smallest_watchlist("abcd"))
print(make_smallest_watchlist("seven"))

# TC: O(n). The two pointers start at the outer edges and move inward toward the center, visiting each character at most once.
# Because you must read every character in the string at least once, O(n) is the theoretical lower bound.
# SC: O(n). In python strings are immutable. Converting the string into a mutable list and rejoining it into a new string requires O(n) auxiliary space, which is unavoidable when constructing the modified result.