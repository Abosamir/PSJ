def removeOuterParentheses(self, s: str) -> str:
    stack = []
    result = ""

    for char in s:
        if char == "(":
            if stack:
                result += "("
            stack.append(char)
        else:
            stack.pop()
            if stack:
                result += ")"
    
    return result