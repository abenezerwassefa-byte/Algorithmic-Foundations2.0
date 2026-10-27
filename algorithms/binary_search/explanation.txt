# BINARY SEARCH

## OVERVIEW

Binary search is an efficient searching algorithm used to find a specific item in a sorted list. Instead of checking every element individually, it repeatedly divides the search interval in half, eliminating the half that cannot contain the target.

IMPORTANT: The list must be sorted in ascending order for this implementation to work correctly.

## HOW IT WORKS

1. Initialize two variables:

   * low: The index of the first element in the search interval (0).
   * high: The index of the last element in the search interval (len(list) - 1).

2. While low <= high, there are still elements to search.

3. Calculate the middle index:
   mid = (low + high) // 2

   The // operator performs floor division, producing an integer index.

4. Retrieve the element at the middle index:
   guess = list[mid]

5. Compare guess with the target item:

   * If guess == item, the target has been found. Return its index.
   * If guess > item, the target must be in the left half. Update high to mid - 1.
   * Otherwise, the target must be in the right half. Update low to mid + 1.

6. If low becomes greater than high, the search interval is empty. The target is not in the list, so return None.

## CODE WALKTHROUGH

def binary_search(list, item):

```
low = 0
high = len(list) - 1

while low <= high:
    mid = (low + high) // 2
    guess = list[mid]

    if guess == item:
        return mid

    if guess > item:
        high = mid - 1
    else:
        low = mid + 1

return None
```

## EXAMPLE

Given:
list = [1, 3, 5, 7, 9, 11, 13]
item = 7

Initial values:
low = 0
high = 6

ITERATION 1:
mid = (0 + 6) // 2 = 3
guess = list[3] = 7

```
Since guess == item, the function returns 3.
```

Result:
3

The target is found at index 3. Remember that Python uses zero-based indexing, so index 3 represents the fourth element.

## WHY THE BOUNDARIES CHANGE

When guess > item:
high = mid - 1

```
The middle element and everything to its right can be excluded
because the list is sorted in ascending order.
```

When guess < item:
low = mid + 1

```
The middle element and everything to its left can be excluded
for the same reason.
```

The algorithm discards the middle element after comparing it with
the target because that element has already been checked.

## RETURN VALUES

* Returns an integer representing the target's index if found.
* Returns None if the target does not exist in the list.

## TIME COMPLEXITY

Best case:    O(1)
The middle element is the target on the first iteration.

Average case: O(log n)
The search interval is repeatedly divided in half.

Worst case:   O(log n)
The algorithm continues halving the search interval until the
target is found or no elements remain.

## SPACE COMPLEXITY

O(1) auxiliary space.

The algorithm uses a fixed number of variables regardless of the
list's size. This implementation is iterative, so it does not use
recursive function calls or an additional search structure.

## KEY TAKEAWAY

Binary search achieves O(log n) time complexity by eliminating
approximately half of the remaining search interval in each iteration.

Its efficiency depends on the list being sorted and on the ability
to access elements by index in O(1) time, as Python lists allow.
