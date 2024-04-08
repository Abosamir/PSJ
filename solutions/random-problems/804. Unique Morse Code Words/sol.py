def uniqueMorseRepresentations(self, words: list[str]) -> int:
    letter_to_symbol = {
    'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
    'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
    'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
    'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
    'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--",
    'z': "--.."
    }
    final_word = ""
    set_of_symbols = set()
    for word in words:
        for letter in word:
            final_word += letter_to_symbol[letter]
        set_of_symbols.add(final_word)
        final_word = ""
    return len(set_of_symbols)


print(uniqueMorseRepresentations("f",["gin","zen","gig","msg"]))