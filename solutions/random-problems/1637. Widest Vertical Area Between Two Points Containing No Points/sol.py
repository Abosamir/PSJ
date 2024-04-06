def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
    distance = -1
    k = 0
    j = 1
    points = sorted(points)
    while j != len(points):
        new_distance = abs(points[k][0]-points[j][0])
        if new_distance > distance:
            distance = new_distance
            k += 1
            j+= 1
        else:
            k += 1
            j += 1
    return distance


print(maxWidthOfVerticalArea("f",[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))


