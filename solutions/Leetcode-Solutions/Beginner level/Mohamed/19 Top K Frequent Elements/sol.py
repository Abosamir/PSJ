from collections import Counter
def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    
    count = Counter(nums)

    if len(nums) < 2:
        return nums
    else:
        pivot = count[0]
        less = [num for num in nums[1:] if count[num] <= pivot]
        greater = [num for num in nums[1:] if count[num] > pivot]
        return topKFrequent(greater) + pivot + topKFrequent(less)
    

print(topKFrequent('f',[1,1,1,2,2,3],2))