def binary_search_string(arr, x):
    """
    Performs binary search on an array of strings to find the given string.

    Args:
    arr (list): The list of strings to be searched.
    x (str): The string to be searched for.

    Returns:
    int: The index of the string in the array if found, else -1.
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
