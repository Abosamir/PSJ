def isAnagram(self, s: str, t: str) -> bool:
    def make_dict(s: str) -> dict:
        word_dict = {}
        for i in s:
            if i not in word_dict:
                word_dict[i] = 1
            else:
                word_dict[i] += 1
        return word_dict

    return make_dict(s) == make_dict(t)

