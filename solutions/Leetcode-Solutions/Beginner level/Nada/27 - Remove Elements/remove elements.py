class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_list = len(nums)
        while val in nums:
            nums.remove(val)
 
        return len_list