def increasingTriplet(self, nums: list[int]) -> bool:
    triple_exist = 0

    if len(nums)<3:
        return False
    
    for i in range(1, len(nums)):

        if nums[i]>nums[i-1]:
            triple_exist += 1
            
            if triple_exist == 3 :
                return True
        else:
            triple_exist = 1

    return False


print(increasingTriplet("f",[20,100,10,12,5,13]))