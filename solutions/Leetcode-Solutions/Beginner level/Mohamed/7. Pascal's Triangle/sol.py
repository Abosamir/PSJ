def generate(self, numRows: int) -> list[list[int]]:

    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    
    gen_list = [[1],[1,1]]

    for _ in range(numRows-2):

        k, j = 0, 1
        added_list = []
        while j <= len(gen_list[-1])-1:
            number_added = gen_list[-1][k]+ gen_list[-1][j]
            added_list.append(number_added)
            k +=1
            j += 1
        next_row = [1] + added_list + [1]
        gen_list.append(next_row)
    return gen_list


