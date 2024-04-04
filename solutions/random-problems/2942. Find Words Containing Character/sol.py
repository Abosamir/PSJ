def findWordsContaining(self, words: list[str], x: str) -> list[int]:
    i = 0
    list_of_words = []
    for word in words:
        if x in word:
            list_of_words.append(i)
        i += 1
    
    return list_of_words