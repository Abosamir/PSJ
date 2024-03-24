class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        first_str = strs[0]
        prefix_length = len(first_str)
        prefix = ""
        for str in strs[1:]:

            for i in range(prefix_length+1):
                if str[:i] == first_str[:i]:
                    prefix = str[:i]
                else:
                    break
            
            prefix_length = len(prefix)
        
        return prefix