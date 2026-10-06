"""Quick Sort/Divide and Conquer"""
def quick_sort(integer_list: list[int]) -> list[int]:
    """Quick Sort"""
    # Base case: empty lists or single-element lists are already sorted
    if len(integer_list) <= 1:
        return integer_list

    pivot = integer_list[0]

    # Partition into three sublists
    less = [x for x in integer_list if x < pivot]
    equal = [x for x in integer_list if x == pivot]
    greater = [x for x in integer_list if x > pivot]

    # Recursively sort sublists and combine
    return quick_sort(less) + equal + quick_sort(greater)
# try it out
print(quick_sort([5, 2, 8, 5, 1]))
