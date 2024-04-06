class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        layer = size//2
        print(layer)

        for i in range(0,layer):
            first = i
            last = size-first-1
            for j in range(first,last):
                off = j - first
                
    #             top = (first,j)
    #             right = (last,off)
    #             bottom = (last,last-off)
    #             left = (last-off,first)
                
    #             print(f"{top}\n{right}\n{bottom}\n{left}")
                
                top = matrix[first][j]
                right = matrix[j][last]
                bottom = matrix[last][last-off]
                left = matrix[last-off][first]
                
                matrix[first][j] = left
                matrix[j][last] = top
                matrix[last][last-off] = right
                matrix[last-off][first] = bottom
            
