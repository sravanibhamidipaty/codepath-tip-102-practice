# Telephone (Version 1, Problem 8)
"""
Understand
1. What if the start villager is already the target villager?
2. How do you safely prevent a NoneType error or infinite loop?

Plan
1. Initialize a pointer
2. Traverse the chain
3. Check the match
4. Advance the pointer
5. Return False at the end of the list
"""

# Implement
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

def message_received(start_villager, target_villager):
    current = start_villager
    while current is not None:
        if current == target_villager:
            return True
        current = current.neighbor
    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))

# TC: O(n). In the worst case, you traverse through all $n$ villagers in the chain until you either find the target or reach None.
# SC: O(1). You only use a single pointer variable (current) to keep track of your position, using constant extra memory.

# Saharah (Version 1, Problem 11)
"""
Understand
1. How do you bypass or remove the first node?
2. How do you locate the end of the list?

Plan
1. Identify the new head
2. Create the new node
3. Traverse to the tail
4. Append the new node
"""

# Implement
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

current = timmy
while current.next is not None:
    current = current.next

saharah = Node("Saharah")
current.next = saharah

# TC: O(n) where n is the number of nodes in the linked list.
# SC: O(1) because I am only adding one additional node to the linked list

# Print Players Linked List (Version 1, Problem 12)
"""
Understand
1. What should the function return?
2. How do you avoid a trailing separator?

Plan
1. Initialize a list
2. Traverse the linked list
3. Format and return
"""

# Implement

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def print_list(node):
    values = []
    curr = node

    while curr:
        values.append(curr.val)
        curr = curr.next

    return " -> ".join(values)

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))

# TC: O(n) where n is the number of nodes
# SC: O(n) auxiliary space because of the values array