# Reverse a singly linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None 
    current = head 
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Create list: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Reverse it 
new_head = reverse_list(head)

# Print result
curr = new_head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")