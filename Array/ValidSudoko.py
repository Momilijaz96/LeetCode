import numpy as np

class Solution:
    def isValidElem(self,elem):
        unique={}
        for c in elem:
            if (c in unique) and c!='.':
                unique[c]+=1
                return False
            else:
                unique[c]=1
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board=np.array(board)
        for idx in range(9):
            rl=idx-(idx%3)
            cl=0+(3*(idx%3))
            if self.isValidElem(board[idx,:]) and self.isValidElem(board[:,idx]) and self.isValidElem((board[rl:rl+3,cl:cl+3].flatten())):
                pass
            else:
                return False
        return True