class Solution:
    def isPalindrome(self, x: int) -> bool:
        if "-" in str(x):
            return False
        else:
            reversed_num = int(str(x)[::-1])
            if x == reversed_num:
                return True
            else:
                return False
