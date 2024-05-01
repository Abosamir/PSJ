def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'o','e','i','u','A','O','E','I','U']
    s = list(s)
    j = 0
    k = len(s)-1
    
    while k >= j:
        if s[j] not in vowels:
            j += 1
        else:
            if s[k] not in vowels:
                k -= 1
            else:
                temp_var = s[k]
                s[k] = s[j]
                s[j] = temp_var
                j += 1
                k -= 1
    return "".join(s)

print(reverseVowels("f","hello"))


