class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        counts = []
        
        # Iterate through each element in nums
        for i in range(len(nums)):
            count = 0
            # Compare nums[i] with every other element in nums
            for j in range(len(nums)):
                if nums[j] < nums[i] and j != i: # Check if nums[j] is smaller than nums[i] and j is not equal to i
                    count += 1
            counts.append(count) # Append the count to the counts list
        
        return counts
        