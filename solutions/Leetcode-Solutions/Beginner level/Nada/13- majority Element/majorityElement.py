class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output = nums[0]
        dict = {}
        for i in set(nums):
            dict[i] = nums.count(i)
        for key in dict:
            if dict[key]  > dict[output]:
                output = key
        return output
        