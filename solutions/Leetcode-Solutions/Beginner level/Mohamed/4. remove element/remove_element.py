class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        indices_to_remove = []
        for i in range(len(nums)):
            if nums[i] == val:
                indices_to_remove.append(i)
        indices_to_remove.reverse()
        for j in indices_to_remove:
            nums.pop(j)
        return len(nums)