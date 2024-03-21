class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_of_words = s.strip().split(" ")
        return len(list_of_words[-1])
