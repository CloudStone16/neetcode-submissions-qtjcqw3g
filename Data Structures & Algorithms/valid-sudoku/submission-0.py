class Solution:
    def check_grid(self, row, col, grid):
        grid_ele = []
        print(row, col)
        for i in range(row * 3, row * 3 + 3):
            for j in range(col * 3, col * 3 + 3):
                
                if grid[i][j] == '.':
                    continue
                elif grid[i][j] not in grid_ele:
                    grid_ele.append(grid[i][j])
                else:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        col = []
        grid = []
        # Checking row
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] not in row and board[i][j] != '.':
                    row.append(board[i][j])
                else:
                    if board[i][j].isnumeric():
                        print("present in row")
                        return False
                if board[j][i] not in col and board[j][i] != '.':
                    col.append(board[j][i])
                else:
                    if board[j][i].isnumeric():
                        print("present in col")
                        return False
        print("Checking grids")
        # Checking grids
        grid_row = 0
        grid_col = 0
        for grid_row in range(3):
            for grid_col in range(3):
                if not self.check_grid(grid_row, grid_col, board):
                    return False
        return True
                

            
    
                
