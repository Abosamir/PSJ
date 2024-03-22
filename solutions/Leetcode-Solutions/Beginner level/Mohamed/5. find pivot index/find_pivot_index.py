def pivotIndex(self, nums: list[int]) -> int:

    if not nums:
        return -1
    if len(nums) == 1 :
        return 0
    
    nums.insert(0,0)
    nums.append(0)

    for i in range(1, len(nums)-1):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i+1:])

        if left_sum == right_sum:
            return i-1
        
    return -1
