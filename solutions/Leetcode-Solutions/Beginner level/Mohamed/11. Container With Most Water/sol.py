def maxArea(self, height: list[int]) -> int:

    p1 = 0
    p2 = len(height)-1
    max_area = 0
    while p2 > p1:

        width = p2 -p1

        max_area = max(max_area,width*min(height[p1],height[p2]))

        if height[p2]>height[p1]:
            p1 += 1
        else:
            p2 -= 1
    return max_area
