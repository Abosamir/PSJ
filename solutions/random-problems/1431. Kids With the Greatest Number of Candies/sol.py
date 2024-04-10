def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    max_candies = max(candies)
    result = []
    for candi in candies:
        if candi + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result