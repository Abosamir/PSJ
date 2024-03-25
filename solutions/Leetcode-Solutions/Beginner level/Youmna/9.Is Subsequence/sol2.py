def isSubsequence(self, s: str, t: str) -> bool:

    iterator = iter(t)

    return all(char in iterator for char in s)