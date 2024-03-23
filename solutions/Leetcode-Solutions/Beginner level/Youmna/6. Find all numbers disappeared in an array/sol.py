class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums: #4
            index = abs(num) - 1 #3
            nums[index] = -abs(nums[index]) # -7 [4,3,2,-7,8,2,3,1]

        return [i + 1 for i, num in enumerate(nums) if num > 0]