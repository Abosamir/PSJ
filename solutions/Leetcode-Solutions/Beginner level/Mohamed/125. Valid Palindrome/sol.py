def isPalindrome(self, s: str) -> bool:
    p1 = 0
    p2 = len(s)-1
    
    while p2 > p1:

        while p2 > p1 and s[p1].isalnum() == False:
            p1 += 1
        
        while p2 > p1 and s[p2].isalnum() == False:
            p2 -= 1

        if s[p1].lower() == s[p2].lower():
            p1 += 1
            p2 -= 1
        else:
            return False

    return True

print(isPalindrome("f", "0p"))