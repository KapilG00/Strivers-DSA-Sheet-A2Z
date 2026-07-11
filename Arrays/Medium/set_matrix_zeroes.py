from typing import List



def set_matrix_zeroes(matrix: List[List[int]]) -> List[List[int]]:
    matrix_rows = len(matrix)

    for i in range(matrix_rows):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                print("INSIDE IF")
                # mark the corresponding row as '0'
                k = len(matrix[i])-1
                print("K:", k)
                print("matrix before:", matrix)
                while k > -1:
                    matrix[i][k] = 0
                    k -= 1
                    print("matrix after:", matrix)    


                # mark the corresponding column as '0'



if __name__ == "__main__":
    print(set_matrix_zeroes([[1,1,1], [1,0,1], [1,1,1]]))