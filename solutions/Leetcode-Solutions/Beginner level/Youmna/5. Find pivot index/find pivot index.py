class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums) 
        left_list=0 
        for i in range(len(nums)) :
            right_list=total-nums[i]-left_list 
            if left_list==right_list:
                return i 
            left_list+=nums[i]
        return -1