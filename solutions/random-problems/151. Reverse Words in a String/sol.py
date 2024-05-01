def reverseWords(self, s: str) -> str:
    s = s.split()
    return " ".join(list(reversed(s)))



print(reverseWords("f","  hello world  "))