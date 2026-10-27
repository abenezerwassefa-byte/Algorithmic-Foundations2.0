class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, values):
        self.head = None

        for value in values:
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
            else:
                current = self.head

                while current.next is not None:
                    current = current.next

                current.next = new_node

    def __str__(self):
        values = []

        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        return " → ".join(values)


# Our normal Python list
values = [10, 21, 90, 240, 510, 33, 15]

# Create a linked list from it
linked_list = LinkedList(values)

# Print the linked list
print(linked_list)
