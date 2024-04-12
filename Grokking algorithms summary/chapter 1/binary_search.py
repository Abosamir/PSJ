def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = (low + high) //2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid +1
    return None


print(binary_search([1,2,3,4,5,6,7,8,9],3))