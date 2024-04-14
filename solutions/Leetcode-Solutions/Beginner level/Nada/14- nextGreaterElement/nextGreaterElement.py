class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for x in nums1:
            index = nums2.index(x)
            if index > len(nums2)-1:
                output.append(-1)
            for i in nums2[index:]:
                if i > nums2[index]:
                    output.append(i)
                    break 
            else:
                output.append(-1)
        return output