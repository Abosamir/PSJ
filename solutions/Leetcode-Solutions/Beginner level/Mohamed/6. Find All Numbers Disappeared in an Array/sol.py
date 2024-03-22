def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    set1 = set(range(1,len(nums)+1))
    set2 = set(nums)

    return list(set1.difference(set2))



print(findDisappearedNumbers("f",[1,1]))