def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
    i = 0
    list_of_indices = []
    k = 0
    while i <= len(nums1)-1:
        if nums2[k] != nums1[i]:
            k += 1
        else:
            k += 1
            while k<= len(nums2):
                if k == len(nums2):
                    list_of_indices.append(-1)
                    i += 1
                    break
                if nums2[k] > nums1[i]:
                    list_of_indices.append(nums2[k])
                    i += 1
                    break
                else:
                    k += 1
            k = 0
    return list_of_indices