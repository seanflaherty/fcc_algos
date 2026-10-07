"""Function that implements the selection sort algorithm."""
def selection_sort(list_to_sort):
    """sort algorithm"""
    n = len(list_to_sort)
    for i in range(n):
        # Assume the current position holds the minimum
        min_index = i

        # Scan the unsorted portion to find the true minimum
        for j in range(i + 1, n):
            if list_to_sort[j] < list_to_sort[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        if min_index != i:
            list_to_sort[i], list_to_sort[min_index] = (
                list_to_sort[min_index],
                list_to_sort[i],
            )

    return list_to_sort
