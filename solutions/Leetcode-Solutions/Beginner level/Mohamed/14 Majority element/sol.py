def majorityElement(self, nums: list[int]) -> int:

    dict_numbers = {}

    for num in nums:
        if num not in dict_numbers:
            dict_numbers[num] = 1
        else:
            dict_numbers[num] += 1
    max_key = max(dict_numbers, key=dict_numbers.get)  # Find the key associated with the highest value
    return max_key

