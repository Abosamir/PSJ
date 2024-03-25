class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Two pointers: i for s, j for t
        while i < len(s) and j < len(t):  # Iterate while both strings have characters to check
            if s[i] == t[j]:
                i += 1  # Increment i only if characters match
            j += 1  # Always increment j to move forward in t
        return i == len(s)  # Return True if all characters in s found in t (i reaches end of s)  