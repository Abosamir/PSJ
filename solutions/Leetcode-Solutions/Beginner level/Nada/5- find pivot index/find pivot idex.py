class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_list= nums[:i]
            right_list= nums[i+1:]
            sum_left_list=sum(left_list)
            sum_right_list= sum(right_list)
            if sum_left_list == sum_right_list:
                return i
        else:
            return -1
        