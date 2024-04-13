def interpret(self, command: str) -> str:
    return command.replace("()","o").replace("(","").replace(")","")


print(interpret("f","G()()()()(al)"))