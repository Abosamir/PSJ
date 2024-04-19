class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        charToWords = {}
        wordToChar = {}

        for c , w in zip (pattern , words):
            if c in charToWords and charToWords[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWords[c] = w
            wordToChar[w] =c
        return True
        