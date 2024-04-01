def replaceElements(self, arr: list[int]) -> list[int]:
    
    arr = list(reversed(arr))

    max_right_arr = []
    if not arr or len(arr) == 1:
        return [-1]
    
    greater = arr[0]
    for i in range(1,len(arr)):
        greater = max(arr[i-1],greater)
        max_right_arr.append(greater)
    
    return list(reversed(max_right_arr))+[-1]
