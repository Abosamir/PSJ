def longestConsecutive(self, nums: list[int]) -> int:

    if not nums:
        return 0
    
    sort_nums = sorted(nums)

    consecutive = 1
    max_consecutive = 1
    for i in range(1,len(sort_nums)):
        if sort_nums[i] == sort_nums[i-1]+1:
            consecutive += 1
        elif sort_nums[i] > sort_nums[i-1]+1:
            max_consecutive = max(consecutive,max_consecutive)
            consecutive = 1
    return max(consecutive,max_consecutive)


print(longestConsecutive("f",[0,3,7,2,5,8,4,6,0,1]))