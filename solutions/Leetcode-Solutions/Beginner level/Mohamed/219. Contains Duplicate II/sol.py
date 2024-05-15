def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    p1 = 0
    p2 = 1

    while p2 < len(nums):

        if p2 - p1 > k:
            p1 += 1
        
        else:
            if nums[p2] in nums[p1:p2] and p2 - p1 <= k:
                return True
            else:
                p2 += 1
    return False




print(containsNearbyDuplicate("F",[1,2,3,1,2,3], k = 2))