def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if not nums2:
        return nums1
    p1 = m
    p2 = 0
    while n != 0:
        nums1[p1] = nums2[p2]
        p2 += 1
        p1 += 1
        n -=1
    return nums1.sort()