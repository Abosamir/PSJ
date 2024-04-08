class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        for i, char in enumerate(s):
            if i < len(s) - 1:
                if char == "I" and s[i + 1] in ["V", "X"]:
                    sum -= roman_to_int_dict[char]
                elif char == "X" and s[i + 1] in ["L", "C"]:
                    sum -= roman_to_int_dict[char]
                elif char == "C" and s[i + 1] in ["D", "M"]:
                    sum -= roman_to_int_dict[char]
                else:
                    sum += roman_to_int_dict[char]
            else:
                sum += roman_to_int_dict[char]

        return sum



        