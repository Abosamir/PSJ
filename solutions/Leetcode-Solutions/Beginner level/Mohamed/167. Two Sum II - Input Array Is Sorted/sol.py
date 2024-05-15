def twoSum(self, numbers: list[int], target: int) -> list[int]:
    
    p1 = 0
    p2 = len(numbers)-1

    while p2 > p1:
        pointers_sum = numbers[p1]+numbers[p2]

        if pointers_sum > target:
            p2 -= 1
        elif pointers_sum < target:
            p1 += 1
        else:
            return [p1+1,p2+1]