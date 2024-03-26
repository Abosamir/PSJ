def test_word(word_1, word_2):
    i = 0
    k = 0
    dict_letters = {}
    for _ in range(len(word_1)):
        if word_1[i] not in dict_letters:
            dict_letters[word_1[i]] = word_2[k]
            i += 1
            k += 1
        elif word_1[i] in dict_letters and dict_letters[word_1[i]] == word_2[k]:
            i +=1 
            k +=1
        else:
            return False
    return True

def isIsomorphic(self, s: str, t: str) -> bool:

    if not test_word(word_1=s, word_2=t):
        return False

    if not test_word(word_1=t, word_2=s):
        return False

    return True



print(isIsomorphic("f","paper","title"))

