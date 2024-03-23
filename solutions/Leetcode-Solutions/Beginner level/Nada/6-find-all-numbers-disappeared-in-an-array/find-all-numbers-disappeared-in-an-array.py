class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        expected_numbers = set(range(1, len(nums) + 1))  # Set of expected numbers
        set_nums = set(nums)  # Set of actual numbers in the input array
        return list(expected_numbers.difference(set_nums))  # Find missing numbers