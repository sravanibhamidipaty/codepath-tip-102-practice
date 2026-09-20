# Merge Sort Playlist (Problem Set 2, Problem 6)

"""
Understand
1. Should the original list be modified in-place, or should a new sorted list be returned?
2. How should edge cases like empty lists or single-element lists be handled?

Plan
merge_sort_helper(left_arr, right_arr)
1. Initialize an empty list result and two index pointers i = 0 and j = 0.
2. Compare strings at left_arr[i] and right_arr[j]:
    - Append the alphabetically smaller (or equal) string to result and increment its pointer.
3. Once one array is fully traversed, append any remaining elements from left_arr[i:] or right_arr[j:] to result.
4. Return result

merge_sort_playlist(playlist)
1. Base Case: if len(playlist) <= 1, return playlist
2. Divide: Find the midpoint mid = left + (right-left)//2. Slice playlist into left_half and right_half
3. Conquer: Recursively sort both halves:
    - sorted_left = merge_sort_playlist(left_half)
    - sorted_right = merge_sort_playlist(right_half)
4. Combine: Pass sorted_left and sorted_right into merge_sort_helper() and return the merged list.
"""

# Implement
def merge_sort_helper(left_arr, right_arr):
    result = []
    left_ptr = 0
    right_ptr = 0
    left_length = len(left_arr)
    right_length = len(right_arr)

    while left_ptr < left_length and right_ptr < right_length:
        if left_arr[left_ptr] < right_arr[right_ptr]:
            result.append(left_arr[left_ptr])
            left_ptr += 1
        else:
            result.append(right_arr[right_ptr])
            right_ptr += 1

    result.extend(left_arr[left_ptr:])
    result.extend(right_arr[right_ptr:])
    return result

def merge_sort_playlist(playlist):
    if len(playlist) <= 1:
        return playlist

    mid = len(playlist)//2
    left_half = playlist[:mid]
    right_half = playlist[mid:]

    sorted_left = merge_sort_playlist(left_half)
    sorted_right = merge_sort_playlist(right_half)
    return merge_sort_helper(sorted_left, sorted_right)

print(merge_sort_playlist(["Formation", "Crazy in Love", "Halo"]))
print(merge_sort_playlist(["Single Ladies", "Love on Top", "Irreplaceable"]))

# TC: O(n log n) where n is the number of songs in playlist. Splitting the list in half takes log n recursive levels,
# and merging the elements across each level takes O(n) string comparisons.
# SC: O(n) auxiliary space to store the merged sub-lists and slices during recursion (plus O(log n) call stack depth).

# Cruise Ship Treasure Hunt (Problem Set 1, Problem 6)

"""
Understand
1. What should be returned if the matrix is empty (e.g., [] or [[]])?
2. What if the target value appears multiple times in the matrix?

Plan
1. Handle Edge Cases: If matrix is empty or matrix[0] is empty, return (-1, -1).
2. Initialize Dimensions & Pointers:
    - Set rows = len(matrix) and cols = len(matrix[0]).
    - Start pointer at top-right corner: row = 0, col = cols - 1.
3. Search Space Reduction Loop:
    - While row < rows and col >= 0:
        - If matrix[row][col] == treasure:
            - Found target; return (row, col).
        - Elif matrix[row][col] < treasure:
            - Target is larger than everything to the left in this row. Move down: row += 1.
        - Else (matrix[row][col] > treasure):
            - Target is smaller than everything below in this column. Move left: col -= 1.
4. Return (-1, -1) if the target is not found after exiting the loop.
"""

# Implement
def find_treasure(matrix, treasure):
    if not matrix or not matrix[0]:
        return (-1, -1)

    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols-1

    while row < rows and col >= 0:
        if matrix[row][col] == treasure:
            return (row, col)
        elif matrix[row][col] < treasure:
            row += 1
        else:
            col -= 1

    return (-1, -1)

rooms = [
    [1, 4, 7, 11],
    [8, 9, 10, 20],
    [11, 12, 17, 30],
    [18, 21, 23, 40]
]

print(find_treasure(rooms, 17))
print(find_treasure(rooms, 5))

# TC: O(m + n), where m is the number of rows and n is the number of columns. O(m + n), where m is the number of rows
# and n is the number of columns. At most, we make m + n moves before reaching a boundary.
# SC: O(1) auxiliary space because we only use a fixed set of pointer variables (rows, cols, row, col).

# Determining Profitability of Excursions (Problem Set 1, Problem 4)

"""
Understand
1. How is x defined relative to array indices?
2. What condition makes x valid?

Plan
1. Handle Edge Cases: If excursion_counts is empty, return -1.
2. Initialize Binary Search Range:
    - Set left = 0 and right = n - 1 where n is len(excursion_counts).
3. Binary Search Loop (while left <= right):
    - Calculate mid = (left + right) // 2.
    - Define candidate x = n - mid.
    - If excursion_counts[mid] >= x:
        - There are at least x excursions with >= x passengers. x could be a valid answer or the true x might be even 
        larger (which corresponds to a smaller index).Search the left half: right = mid - 1.
    - Else (excursion_counts[mid] < x):
        - There are fewer than x excursions with >= x passengers. x is too large, so we need a smaller x (which 
        corresponds to a larger index).Search the right half: left = mid + 1.
4. Validation Check:
    - After the loop finishes, left points to the insertion boundary.
    - If left < n:
        - Set x = n - left.
        - Check if excursion_counts[left] >= x AND (left == 0 or excursion_counts[left - 1] < x).
        - If both conditions hold, return x.
5. Return -1 if no valid x exists.
"""

# Implement
def is_profitable(excursion_counts):
    if not excursion_counts:
        return -1

    n = len(excursion_counts)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        x = n - mid

        if excursion_counts[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1

    if left < n:
        x = n - left
        at_least_x = excursion_counts[left] >= x
        no_more_than_x = left == 0 or excursion_counts[left - 1] < x

        if at_least_x and no_more_than_x:
            return x

    return -1

# TC: O(log n), where n is the number of elements in excursion_counts. The binary search halves the search space in
# each iteration, running in logarithmic time.
# SC: O(1) auxiliary space because the search uses only a few integer variables (left, right, mid, x).