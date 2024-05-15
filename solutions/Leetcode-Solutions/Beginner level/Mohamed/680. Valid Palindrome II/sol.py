def isPalindrome(self, s: str, p1: int, p2: int) -> bool:
    while p2 > p1:
        if s[p2] != s[p1]:
            return False
        p2 -= 1
        p1 += 1
    return True
def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        
        while p2 > p1:
            if s[p2] == s[p1]:
                p2 -= 1
                p1 += 1
            else:
                return self.isPalindrome(s, p1 + 1, p2) or self.isPalindrome(s, p1, p2 - 1)
        
        return True