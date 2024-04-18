def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

    anagrams = {}


    for word in strs:

        new_word = "".join(sorted(word))

        if new_word not in anagrams:

            anagrams[new_word] = [word]
        else:
            anagrams[new_word].append(word)

    return list(anagrams.values())
    

print(groupAnagrams("F",["a"]))



