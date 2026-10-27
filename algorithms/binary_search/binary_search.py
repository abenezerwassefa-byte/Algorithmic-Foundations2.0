def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:  # while there are elements to look between high and low
        # these are the indices
        mid = (low + high) // 2  # flooring the middle index
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


binary_search([1, 2, 3, 4, 5, 34, 45], 5)
