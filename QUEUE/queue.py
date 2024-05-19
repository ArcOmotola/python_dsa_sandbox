# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         """Check if the queue is empty."""
#         return len(self.items) == 0

#     def enqueue(self, item):
#         """Add an item to the rear of the queue."""
#         self.items.append(item)

#     def dequeue(self):
#         """Remove and return the item from the front of the queue."""
#         if not self.is_empty():
#             return self.items.pop(0)
#         raise IndexError("dequeue from an empty queue")

#     def peek(self):
#         """Get the item at the front of the queue without removing it."""
#         if not self.is_empty():
#             return self.items[0]
#         raise IndexError("peek from an empty queue")

#     def size(self):
#         """Return the number of items in the queue."""
#         return len(self.items)


class Node:
    def __init__(self, value=None):
       self.value = value
       self.prev = None
       self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """Check if the queue is empty."""
        return self.head is None

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        new_node = Node(item)
        if self.tail is None:  # Queue is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            return None

        original_head = self.head.value
        new_head = self.head.next
        self.head = new_head

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return original_head

    def peek(self):
        """Get the item at the front of the queue without removing it."""
        if self.is_empty():
            return None
        return self.head.value  # Corrected to return the value of the head

    def queue_size(self):
        """Return the number of items in the queue."""
        counter = 0
        curr = self.head  # Start counting from the head
        while curr:  # Continue until the end of the list
            counter += 1
            curr = curr.next
        return counter  # Correctly counts all nodes
