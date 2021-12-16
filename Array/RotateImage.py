class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dim=len(matrix)

        for idx in range(dim//2):
            temp=matrix[idx]
            matrix[idx]=matrix[-1*(idx+1)]
            matrix[-1*(idx+1)]=temp
            #print(matrix)
        for row in range(dim):
            for col in range(dim):
                if row<col:
                    temp=matrix[row][col]
                    matrix[row][col]=matrix[col][row]
                    matrix[col][row]=temp