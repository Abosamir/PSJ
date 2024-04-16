def maxDepth(self, s: str) -> int:
    result = 0
    current_value = 0
    for i in s:
        if i == "(":
            current_value += 1
        elif i == ")":
            current_value -= 1
        
        if current_value > result:
            result = current_value
    
    return result

print(maxDepth("f","(1+(2*3)+((8)/4))+1"))