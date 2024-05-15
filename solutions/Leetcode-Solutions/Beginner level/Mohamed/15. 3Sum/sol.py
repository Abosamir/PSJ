def threeSum(self, nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        left, right = i +1 , len(nums)-1

        while right > left:
            three_sum = a + nums[left] + nums[right]

            if three_sum > 0 :
                right -= 1

            elif three_sum < 0 :
                left += 1
            
            else:
                res.append([a,nums[left], nums[right]])
                left += 1




print(threeSum("f",[-1,0,1,2,-1,-4]))