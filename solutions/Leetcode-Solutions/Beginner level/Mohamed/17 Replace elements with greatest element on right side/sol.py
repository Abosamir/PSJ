def replaceElements(self, arr: list[int]) -> list[int]:
    if not arr:
        return []

    max_right = -1
    n = len(arr)

    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_right
        max_right = max(max_right, temp)

    return arr

