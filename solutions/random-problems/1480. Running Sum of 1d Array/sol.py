def runningSum(self, nums: list[int]) -> list[int]:
    result = []
    added_element = 0
    for num in nums:
        added_element += num
        result.append(added_element)
    return result