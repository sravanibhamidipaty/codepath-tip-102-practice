# Validating HTML Tags (Version 1, Problem 5)

"""
Understand
1. How do we handle text or spaces between tags?
2. What if the string begins with a closing tag?

Plan
1. Extract all tags
2. Initialize a stack
3. Iterate through each tag and check if it is a closing tag see if
the opening tag exists. Otherwise, return False.
4. See that there are no additional opening tags left in the stack with the condition len(stack) == 0 at the end.
"""

def validate_html_tags(html: str) -> bool:
    stack = []
    i = 0
    n = len(html)

    while i < n:
        if html[i] == "<":
            end_idx = html.find(">", i)
            tag = html[i:end_idx+1]

            if tag[1] == "/":
                if not stack:
                    return False
                opening_tag = stack.pop()
                if opening_tag[1:] != tag[2:]:
                    return False
            else:
                stack.append(tag)
            i = end_idx + 1
        else:
            i += 1

    return len(stack) == 0

html = "<div><p></p></div>"
print(validate_html_tags(html))

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))

# TC: O(n) where n is the length of the string to parse the tags, and stack operations (push/pop) take O(1) time.
# SC: O(n) because the total number of characters stored across all elements in the stack at any given time can never
# exceed the total length of the input string n.

from datetime import datetime
# Track Popular Destinations (Version 1, Problem 8)
"""
Understand
1. How do we handle ties if multiple destinations have the exact same highest visit count?
2. What should the output format be?

Plan
1. Initialize a dictionary to count total visits per destination, and another dictionary to store the latest visit date
for each destination.
2. Iterate through each (destination, date) tuple in the input list:
    - Update the frequency count.
    - Update the latest date if the current date is chronologically newer than the previously recorded date.
3. Iterate through the tracked destinations to find the one with the maximum visit count.
    - If a tie occurs (equal counts), compare their latest visit dates and pick the one with the more recent timestamp.
4. Return a tuple of the winning destination and its total visit count.
"""

# Implement
def most_popular_destination(visits):
    destination_counts = {}
    destination_latest_date = {}

    for destination, date_str in visits:
        destination_counts[destination] = destination_counts.get(destination, 0) + 1
        current_date = datetime.strptime(date_str, "%Y-%m-%d")

        if (destination not in destination_latest_date or current_date > destination_latest_date[destination]):
            destination_latest_date[destination] = current_date

    best_destination = None
    max_count = -1
    latest_date = None

    for destination, count in destination_counts.items():
        date = destination_latest_date[destination]

        if count > max_count:
            max_count = count
            best_destination = destination
            latest_date = date
        elif count == max_count:
            if date > latest_date:
                best_destination = destination
                latest_date = date

    return (best_destination, max_count)

visits = [("Paris", "2024-07-15"), ("Tokyo", "2024-08-01"), ("Paris", "2024-08-05"), ("New York", "2024-08-10"), ("Tokyo", "2024-08-15"), ("Paris", "2024-08-20")]
print(most_popular_destination(visits))

visits_2 = [("London", "2024-06-01"), ("Berlin", "2024-06-15"), ("London", "2024-07-01"), ("Berlin", "2024-07-10"), ("London", "2024-07-15")]
print(most_popular_destination(visits_2))

visits_3 = [("Sydney", "2024-05-01"), ("Dubai", "2024-05-15"), ("Sydney", "2024-05-20"), ("Dubai", "2024-06-01"), ("Dubai", "2024-06-15")]
print(most_popular_destination(visits_3))

# TC: O(n) where n is the number of tuples of visits.
# SC: O(n) if all places are unique in the worst case for the dictionary.

# Reorder Podcast Episodes (Version 2, Problem 7)
"""
Understand
1. What do the indices mean?
2. Are the indices guaranteed to be valid and unique?

Plan
1. Zip the stack and indices together. Combine stack and indices using zip(stack, indices) to create pairs of (episode,
target_index).
2. Initialize a result list: Create a list with all 0s.
3. Place items into their target postions.
4. Return the result list.
"""

# Implement
def reorder_stack(stack, indices):
    result = [0] * len(stack)

    for episode, target_index in zip(stack, indices):
        result[target_index] = episode

    return result

stack1 = ['Episode1', 'Episode2', 'Episode3', 'Episode4']
indices = [2, 0, 3, 1]
print(reorder_stack(stack1, indices))

stack2 = ['A', 'B', 'C', 'D']
indices = [1, 2, 3, 0]
print(reorder_stack(stack2, indices))

stack3 = ['Alpha', 'Beta', 'Gamma']
indices = [0, 2, 1]
print(reorder_stack(stack3, indices))

# TC: O(n). zip() itself takes O(1) time because it just creates the lazy iterator object (setting up pointers without
# copying anything upfront). The for loop traversal takes O(n) time because the loop consumes the iterator, stepping
# through all n elements one by one to place them into your result array.
# SC: O(1) auxiliary excluding the result array.