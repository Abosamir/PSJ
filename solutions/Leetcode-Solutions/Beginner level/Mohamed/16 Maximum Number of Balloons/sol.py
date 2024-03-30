def maxNumberOfBalloons(self, text: str) -> int:
    num_of_bs = text.count('b')
    num_of_as = text.count('a')
    num_of_ls = text.count('l') // 2
    num_of_os = text.count('o') // 2
    num_of_ns = text.count('n')

    return min(num_of_bs,num_of_as,num_of_ls,num_of_os, num_of_ns)

print(maxNumberOfBalloons("f","loonbalxballpoon"))
