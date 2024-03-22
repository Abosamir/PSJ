class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums :
            first = len(nums)
            nums.remove(val)
        return len(nums)