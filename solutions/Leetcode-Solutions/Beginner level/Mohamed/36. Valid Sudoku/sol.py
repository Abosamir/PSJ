def isValidSudoku(self, board: list[list[str]]) -> bool:

    column_numbers = []
    
    for i in range(9):
        for j in range(9):

            column_num = board[j][i]
            if (column_num in range(1,10)) or (column_num in column_numbers) and (column_num != "."):
                return False
            else:
                column_numbers.append(column_num)
        
        column_numbers = []

    row_numbers = []
    for i in range(9):
        for j in range(9):
            row_num = board[i][j]
            if (row_num in range(1,10)) or (row_num in row_numbers) and (row_num != "."):
                return False
            else:
                row_numbers.append(row_num)
        
        row_numbers = []

    list_of_boxes = [
    [num for row in board[i:i+3] for num in row[j:j+3]]
    for i in range(0, 9, 3)
    for j in range(0, 9, 3)
]
    valid_box = []
    for box in list_of_boxes:
        for num in box:
            if num not in valid_box:
                valid_box.append(num)
            elif num in valid_box and num != ".":
                return False
        valid_box = []
    return True














