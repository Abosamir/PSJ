class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1 = len(nums)
        nums2 = len(set(nums))
        if nums1 == nums2 :
            return False   
        else:
            return True 