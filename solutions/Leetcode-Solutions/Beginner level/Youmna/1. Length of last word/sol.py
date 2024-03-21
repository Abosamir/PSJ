class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split().strip()
        return len(s[-1])