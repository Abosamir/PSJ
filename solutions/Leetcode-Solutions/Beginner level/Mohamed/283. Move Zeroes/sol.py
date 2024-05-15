def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    number_of_zero= 0
    while 0 in nums:
        number_of_zero += 1
        nums.remove(0)
    
    while number_of_zero:
        nums.append(0)
        number_of_zero -=1
