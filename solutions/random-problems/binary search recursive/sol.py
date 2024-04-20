def binary_search_recursive(array, target, left, right):
    # Base case: If left index is greater than right index, target not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # If target is found at mid, return mid
    if array[mid] == target:
        return mid
    
    # If target is smaller than mid element, search left half
    elif target < array[mid]:
        return binary_search_recursive(array, target, left, mid - 1)
    
    # If target is greater than mid element, search right half
    else:
        return binary_search_recursive(array, target, mid + 1, right)
