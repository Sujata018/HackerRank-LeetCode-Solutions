class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols=len(matrix),len(matrix[0])
        firstRowHasZero=False
        for col in range(cols):
            if matrix[0][col]==0:
                firstRowHasZero = True
                break
        firstColHasZero=False
        for row in range(rows):
            if matrix[row][0]==0:
                firstColHasZero = True
                break
            
        for row in range(1,rows):
            setRowZero=False
            allColsZero=True
            for col in range(1,cols):
                if matrix[0][col]!=0: 
                    allColsZero=False
                if matrix[row][col]==0:
                    if matrix[0][col]!=0: 
                        matrix[0][col]=0
                    if setRowZero == False:
                        setRowZero = True
            if setRowZero == True:
                matrix[row][0]=0
            if allColsZero == True:
                break
        for i in range(1,rows):
            if matrix[i][0] == 0:
                matrix[i]=[0 for _ in range(cols)]
        for i in range(1,cols):
            if matrix[0][i] == 0:
                for j in range(1,rows):
                    matrix[j][i]=0
        if firstRowHasZero==True:
            matrix[0]=[0 for _ in range(cols)]
        if firstColHasZero==True:
            for j in range(rows):
                matrix[j][0]=0
                
if __name__=='__main__':
    m=Solution()
    mat=[[1,1,1],[1,0,1],[1,1,1]]
    m.setZeroes(mat)
    if mat == [[1, 0, 1], [0, 0, 0], [1, 0, 1]] :  print("ok")
    else : print('not ok: ',mat)

    mat=[[1,0]]
    m.setZeroes(mat)
    if mat == [[0, 0]]: print("ok")
    else : print('not ok: ',mat)

    mat=[[0,1,3,4],[1,2,4,0],[3,7,2,5]]
    m.setZeroes(mat)
    if mat == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 7, 2, 0]] :   print("ok")
    else : print('not ok: ',mat)

    mat=[[1],[0]]
    m.setZeroes(mat)
    if mat == [[0], [0]] :   print("ok")
    else : print('not ok: ',mat)
    
    mat=[[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
    m.setZeroes(mat)
    if mat == [[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]] :   print("ok")
    else : print('not ok: ',mat)

    mat=[[1,1,0],[-8,6,-8],[0,1,1]]
    m.setZeroes(mat)
    if mat == [[0,0,0],[0,6,0],[0,0,0]] :   print("ok")
    else : print('not ok: ',mat)

    mat=[[8,3,6,9,7,8,0,6],[0,3,7,0,0,4,3,8],[5,3,6,7,1,6,2,6],[8,7,2,5,0,6,4,0],[0,2,9,9,3,9,7,3]]
    m.setZeroes(mat)
    if mat == [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,3,6,0,0,6,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] :   print("ok")
    else : print('not ok: ',mat)
