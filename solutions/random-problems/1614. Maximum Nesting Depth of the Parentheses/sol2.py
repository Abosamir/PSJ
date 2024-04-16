def maxDepth(self, s: str) -> int:
    stack = []
    max_depth = 0
    current_state = 0

    for char in s:
        if char == "(":
            stack.append(char)
            current_state = len(stack)
            max_depth = max(max_depth,current_state)
        elif char == ")":
            stack.pop()
            current_state = len(stack)
    return max_depth
