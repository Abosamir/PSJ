class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]  # Initialize prefix with the first string

        for string in strs[1:]:
            # Iterate over characters of prefix and corresponding characters of string
            for i, char in enumerate(prefix):
                if i == len(string) or char != string[i]:
                    prefix = prefix[:i]  # Update prefix to match until previous character
                    break
        
        return prefix