# Trending Meme Pairs (Version 2, Problem 5)
"""
Understand
1. What is the structure of the input nft_collections?
2. What should be returned if no NFTs contain the specified tag?

Plan
1. Initialize an empty list result to store the names of matching NFTs.
2. Iterate through each collection in nft_collections.
3. Iterate through each individual NFT dictionary within the current collection.
4. Check if the target tag is present in the nft["tags"] list (if tag in nft["tags"]:)
    - If it is, append nft["name"] to result.
5. Return the result list.
"""

# Implement
def search_nft_by_tag(nft_collections: list[dict[str]], tag: str) -> list[str]:
    result = []
    for collection in nft_collections:
        for nft in collection:
            for t in nft["tags"]:
                if t == tag:
                    result.append(nft["name"])

    return result

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))

# TC: O(N x T) where N is the total number of NFTs across all collections, and T be the maximum number
# of tags any single NFT possesses. We visit every NFT once through the nested loops and checking tag in nft["tags"]
# taks time proportional to the number of tags on that NFT (O(T)). In the worst case, this results in linear time
# relative to total items and tags.

# SC: O(1) auxiliary space since only loop variablesa nd a results reference are maintained.

# Search for Viral Meme Groups (Version 2, Problem 7)
"""
Understand
1. Since the meme list is already sorted by popularity scores, how can we leverage this sorted property efficiently?
2. What should be done if an exact sum match to the target is found?

Plan
1. Initialize two pointers: left = 0 at the start and right = len(memes)-1 at the end of the memes list.
2. Initialize min_diff = float('inf') and best_pair = ("", "").
3. Loop while left < right:
    - Unpack the names and scores for both pointers.
    - Calculate the current sum and update the global diff if necessary.
4. Return best_pair.
"""

# Implement
def find_closest_meme_pair(memes, target):
    left = 0
    right = len(memes)-1
    min_diff = float('inf')
    best_pair = ("", "")

    while left < right:
        name1, score1 = memes[left]
        name2, score2 = memes[right]
        current_sum = score1 + score2
        diff = abs(current_sum - target)

        if diff < min_diff:
            min_diff = diff
            best_pair = (name1, name2)

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return (name1, name2)

    return best_pair

memes_1 = [("Distracted boyfriend", 5), ("Dogecoin to the moon!", 7), ("One does not simply walk into Mordor", 12)]
memes_2 = [("Surprised Pikachu", 2), ("This is fine", 6), ("Expanding brain", 9), ("Y U No?", 15)]
memes_3 = [("Philosoraptor", 1), ("Bad Luck Brian", 4), ("First world problems", 8), ("Y U No?", 13)]

print(find_closest_meme_pair(memes_1, 13))
print(find_closest_meme_pair(memes_2, 10))
print(find_closest_meme_pair(memes_3, 12))

# TC: O(N) where N is the number of memes in the memes list. The left and right pointers start at opposite ends and move
# toward each other, visiting each element at most once. This guarantees a linear scan in O(N) time.
# SC: O(1) since we only use variables for state tracking and no additional data structures.

# Validate NFT Addition (Version 1, Problem 7)
"""
Understand
1. What does it mean for a sequence of NFT actions to be balanced?
2. What should be returned if the sequence is unbalanced or if a "remove" happens prematurely?

Plan
1. Initialize a counter variable to 0 to track the balance of active adds and removes.
2. Iterate through each action in the actions list:
    - If the action is "add", increment counter by 1.
    - If the action is "remove", decrement counter by 1.
    - Immediately check if counter < 0. If it drops below zero, a "remove" happened without preceding "add", so return
    False.
3. After the loop completes, check if counter == 0.
    - Return True if counter == 0 (meaning every add was matched and closed), otherwise return False.
"""

# Implement
def validate_nft_actions(actions: list[str]) -> bool:
    counter = 0

    for action in actions:
        if action == "add":
            counter += 1
        elif action == "remove":
            counter -= 1

        if counter < 0:
            return False

    return counter == 0

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))

# TC: O(N) where N is the number of elements in the actions list.
# SC: O(1) because we only use a single integer variable (counter), requiring no
# additional data structures, giving us constant auxiliary space.