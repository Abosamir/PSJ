def wordPattern(self, pattern: str, s: str) -> bool:
    def pattern_to_word(word_1, word_2):
        i = 0
        k = 0
        pattern_to_word = {}
        for _ in range(min(len(word_1),len(word_2))):
            if word_1[i] not in pattern_to_word:
                pattern_to_word[word_1[i]] = word_2[k]
                i += 1
                k += 1
            elif word_1[i] in pattern_to_word and pattern_to_word[word_1[i]] == word_2[k]:
                i +=1 
                k +=1
            else:
                return False
        return True
    list_of_words = s.split()
    if len(pattern) != len(list_of_words):
        return False
    if not pattern_to_word(word_1=pattern, word_2=list_of_words):
        return False
    elif not pattern_to_word(word_1=list_of_words, word_2= pattern):
        return False
    else:
        return True