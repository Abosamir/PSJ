class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 , i1 in enumerate(nums):
            for index2 , i2 in enumerate(nums):
                if index1 != index2 :
                    if i2 + i1 == target: 
                        return index1,index2 
                else: continue 