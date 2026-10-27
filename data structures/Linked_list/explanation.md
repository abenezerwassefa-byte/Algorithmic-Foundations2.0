# SINGLY LINKED LIST

## OVERVIEW

A singly linked list is a linear data structure consisting of nodes.
Each node stores two things:

1. Data: The value held by the node.
2. Next: A reference to the next node in the list.

Unlike a Python list, whose elements are stored in a dynamic array,
a linked list connects its elements through references between nodes.

The first node is called the head. Each node points to the next node,
and the final node points to None, indicating the end of the list.

This implementation defines a Node class to represent individual
nodes and a LinkedList class to manage the connections between them.

## HOW IT WORKS

1. NODE INITIALIZATION

   The Node class represents an individual node.

   ```
   def __init__(self, data):
       self.data = data
       self.next = None
   ```

   * self.data stores the value passed to the node.
   * self.next stores a reference to the next node.
   * Initially, self.next is None because the node is not yet connected
     to another node.

2. LINKED LIST INITIALIZATION

   The LinkedList class represents the entire linked list.

   ```
   def __init__(self, values):
       self.head = None
   ```

   The head is initially None because the list starts empty.

   The constructor then iterates through the provided values and
   creates a new node for each value.

3. INSERTING THE FIRST NODE

   ```
   if self.head is None:
       self.head = new_node
   ```

   If the list is empty, the new node becomes the head.

   The head provides access to the beginning of the linked list and,
   through the next references, to every subsequent node.

4. INSERTING SUBSEQUENT NODES

   ```
   else:
       current = self.head

       while current.next is not None:
           current = current.next

       current.next = new_node
   ```

   If the list already contains nodes, the algorithm starts at the
   head and traverses the list until it reaches the final node.

   The loop continues while current.next is not None. When the
   condition becomes False, current points to the final node.

   The final node's next reference is then assigned the new node,
   extending the linked list.

5. STRING REPRESENTATION

   ```
   def __str__(self):
       values = []
       current = self.head

       while current is not None:
           values.append(str(current.data))
           current = current.next

       return " → ".join(values)
   ```

   The **str** method defines how the linked list is represented
   when passed to print().

   * An empty Python list is created to collect string representations
     of the node values.
   * current starts at the head.
   * The loop visits each node until current becomes None.
   * Each node's data is converted to a string and appended to values.
   * current = current.next advances traversal to the next node.
   * " → ".join(values) combines the collected strings with arrows
     between them.

   This produces a readable representation of the linked list.

## CODE WALKTHROUGH

class Node:

```
def __init__(self, data):
    self.data = data
    self.next = None
```

class LinkedList:

```
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
```

values = [10, 21, 90, 240, 510, 33, 15]

linked_list = LinkedList(values)

print(linked_list)

## EXAMPLE

Input:

```
values = [10, 21, 90, 240, 510, 33, 15]
```

The LinkedList constructor processes each value and creates a node.

After construction, the nodes are connected in this order:

```
head
 |
 v
[10 | •] → [21 | •] → [90 | •] → [240 | •]
                                      |
                                      v
[15 | None] ← [33 | •] ← [510 | •] ←
```

Conceptually, the actual linked list is:

```
head → 10 → 21 → 90 → 240 → 510 → 33 → 15 → None
```

Each arrow represents a next reference between nodes. The final
node's next reference is None.

When print(linked_list) executes, Python calls the linked list's
**str** method.

Output:

```
10 → 21 → 90 → 240 → 510 → 33 → 15
```

The arrows in the output are characters in a string. They are not
the actual references connecting the nodes.

## IMPORTANT CONCEPTS

1. HEAD

   The head is a reference to the first node. Without it, the list
   would have no direct entry point for traversal.

2. NODE REFERENCES

   Each node's next attribute refers to the next node, not merely
   to its value.

3. TRAVERSAL

   Traversal means visiting nodes sequentially by following their
   next references.

   ```
   current = current.next
   ```

   This moves to the next node. It does not modify the linked list.

4. NONE

   None indicates that a reference points to no object.

   In this implementation, the final node's next attribute is None,
   marking the end of the list.

5. **init**

   The **init** method initializes a new object. Here, it creates
   nodes and connects them to construct the linked list.

6. **str**

   The **str** method returns a human-readable string representation
   of an object. It allows print(linked_list) to display the node
   values in a readable format.

## TIME COMPLEXITY

Let n be the number of values used to construct the linked list.

Construction: O(n²) worst case.

Each new node after the first requires traversing the existing list
to reach its final node.

The total traversal work is proportional to:

```
1 + 2 + 3 + ... + (n - 1)
```

This sum is O(n²).

String representation: O(n) time, assuming the total length of the
string representations is proportional to n.

Each node is visited once, and its data is converted to a string.

Accessing the head: O(1).

The head is stored directly in self.head, so accessing it does not
require traversal.

## SPACE COMPLEXITY

Linked list storage: O(n).

Each input value creates one node, and each node stores its data and
a reference to the next node.

String representation: O(n) auxiliary space.

The **str** method creates a list containing the string
representation of every node's data, then joins those strings into
a single result.

Overall, the linked list itself requires O(n) space for n nodes.

## KEY TAKEAWAY

A singly linked list stores data in nodes connected through
references. The head provides access to the first node, and each
node's next attribute leads to the next node until None marks the end.

This implementation demonstrates node creation, linked list
construction, traversal, reference assignment, and custom string
representation.

One important optimization: maintaining a tail reference would
allow new nodes to be appended in O(1) time per insertion, reducing
the total construction time from O(n²) to O(n).
