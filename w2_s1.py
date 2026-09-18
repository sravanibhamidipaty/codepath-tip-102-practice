# Performer Schedule Pattern (Version 1, Problem 11)
"""
Understand
1. What to return if pattern is empty and schedule is empty?
2. What to return if only pattern is empty?

Plan
1. Look for having 2 dictionaries.
2. If a pattern already exists the same word should repeat otherwise return False.
"""

# Implement
def schedule_pattern(pattern, schedule):
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True

pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))


# Sort Signal Data (Version 2, Problem 11)
"""
Understand
1. What if signals array is empty? What to return?
2. Can I modify the original array?

Plan
1. Modify the original array if you can and return it.
2. If signals is empty or only has one element return it immediately.
"""

# Implement
def frequency_sort(signals):
    if len(signals) == 0 or len(signals) == 1:
        return signals

    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 1

    signals.sort(key=lambda x: (freq[x], -x))

    return signals

signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(frequency_sort(signals1))
print(frequency_sort(signals2))
print(frequency_sort(signals3))

# Final Communication Hub (Version 2, Problem 12)
"""
Understand
1. What if the paths list is empty? What to return?
2. Are the paths going to disconnected meaning there are 2 edges in the path itself that are not connected?

Plan
1. Create a dictionary to store the edges. 
2. Go through the dictionary and see if the values is a key in that dictionary itself.
3. If the key is in the dictionary itself then that is not the final answer. If I find a key that is not in the dictionary itself then I return that value as the final hub.
"""

# Implement
def find_final_hub(paths):
    if not paths:
        return None

    if len(paths) == 1:
        return paths[0][1]

    paths_graph = {}

    for a, b in paths:
        paths_graph[a] = b

    for key, value in paths_graph.items():
        if value not in paths_graph:
            return value

    return None

paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1))
print(find_final_hub(paths2))
print(find_final_hub(paths3))

# TC: O(N) where N is the number of paths, because you iterate through the input list once to build
# the mapping and a second time to check key-value memberships.
# SC: O(N) to store teh dictionary of edges.