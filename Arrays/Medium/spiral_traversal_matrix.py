from typing import List


# n => no. of matrix rows; m => no. of matrix columns
# TC: O(nm)
# SC: O(1)
def spiral_traversal(matrix: List[List[int]]) -> None:
    # n*m matrix
    n = len(matrix) # rows
    m = len(matrix[0]) # columns
    left = 0
    right = m-1
    top = 0
    bottom = n-1
    
    while left <= right and top <= bottom:
        # from left -> right
        for i in range(left, right+1):
            print(matrix[top][i])
        top += 1
    
        # from top -> bottom
        for j in range(top, bottom+1):
            print(matrix[j][right])
        right -= 1

        # from right -> left
        if top <= bottom:
            for k in range(right, left-1, -1):
                print(matrix[bottom][k])
            bottom -= 1            
        
        # from bottom -> top
        if left <= right:
            for l in range(bottom, top-1, -1):
                print(matrix[l][left])
            left += 1

    return   



if __name__ == "__main__":
    print(spiral_traversal([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
    print(spiral_traversal([[1, 2, 3]]))
    print(spiral_traversal([[1], [2], [3]]))