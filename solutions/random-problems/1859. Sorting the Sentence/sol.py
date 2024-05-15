def sortSentence(self, s: str) -> str:
    words_with_index = s.split()
    
    dict_words = {}
    
    for word in words_with_index:
        i = len(word) - 1
        index = int(word[i])
        dict_words[index] = word[:i]
    new_s = ""
    for i in sorted(dict_words):
        new_s += dict_words[i] + " "
    return new_s.strip()