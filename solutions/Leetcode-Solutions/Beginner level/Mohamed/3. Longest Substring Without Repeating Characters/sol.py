def lengthOfLongestSubstring(self, s: str) -> int:

    p1 = 0
    p2 = 0
    set_of_characters = []
    longest_sub = 0
    current_sub = 0

    while p2 != len(s):

        if s[p2] not in set_of_characters:
            set_of_characters.append(s[p2])
            current_sub += 1
            p2 += 1
        else:
            p2 = p1 + 1
            p1 += 1
            longest_sub = max(longest_sub, current_sub)
            set_of_characters = []
            current_sub = 0
    return max(longest_sub, current_sub)

print(lengthOfLongestSubstring("f","dvdf"))