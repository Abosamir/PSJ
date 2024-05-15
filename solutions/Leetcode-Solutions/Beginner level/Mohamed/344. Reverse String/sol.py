def reverseString(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    p2 = len(s) - 1
    p1 = 0

    while p2 > p1:
        temp = s[p1]
        s[p1] = s[p2]
        s[p2] = temp
        p1 += 1
        p2 -= 1