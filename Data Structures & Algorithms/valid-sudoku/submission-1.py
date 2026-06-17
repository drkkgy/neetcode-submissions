class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Rules to validate

        # #1 Unique Row
        # for index in range(0,9):
        #     if set(board[index][:]) != board[index][:]:
        #         return False
        #     if set(board[:][index]) != board[:][index]:
        #         return False
            
        # for i in range(3):
        #     for j in range(3):
        #         if set(board[i:i+3][j:j+3]) == board[i:i+3][j:j+3]:
        #             return False
        # return True

        # cbuff = [[]]*9

        # for i in range(len(board[:][0])):
        #     buff = []
        #     for j in range(len(board[0][:])):
        #         if board[i][j] == ".":
        #             continue
        #         if not buff:
        #             buff.append(board[i][j])
        #         else:
        #             if board[i][j] in buff:
        #                 return False
        #         if cbuff:
        #             if board[i][j] in cbuff[:][j]:
        #                 return False
        #         buff.append(board[i][j])
        #         cbuff[i].append(board[i][j])
            
        # return True
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[r//3,c//3]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])        
        return True


            
            

        
            

        