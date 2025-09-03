# Node for singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head 
        while curr:
            print(curr.data, end =" -> ")
            curr = curr.next
        print("None")

# Example
sl1 = SinglyLinkedList()
sl1.insert_at_end(10)
sl1.insert_at_end(20)
sl1.insert_at_end(30)
sl1.insert_at_end(1.30)
sl1.insert_at_end("Vishwa")
sl1.display()