


def twoSum(self, nums: list[int], target: int) -> list[int]:
    
    index_dict = {}

    for i in range(len(nums)):

        rest = target-nums[i]

        if rest in index_dict:
            return [i,index_dict[rest]]
        
        index_dict[nums[i]] = i
        

