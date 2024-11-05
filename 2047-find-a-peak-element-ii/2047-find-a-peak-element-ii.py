class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        def get_row_index_of_max_element(mat, mid):
            max_element = -float('inf')
            index = -1

            n = len(mat)
            for i in range(n):
                if mat[i][mid] > max_element:
                    max_element = mat[i][mid]
                    index = i

            return index



        
        rows = len(mat)
        cols = len(mat[0])

        low = 0
        high = cols - 1

        while low <= high:
            mid = low + (high - low) // 2

            row_index = get_row_index_of_max_element(mat, mid)

            #then find left and right

            if mid - 1 >=0:
                left = mat[row_index][mid-1]

            else:
                left = float('-inf')


            if mid + 1 < cols:
                right = mat[row_index][mid+1]

            else:
                right = float('-inf')

            
            if mat[row_index][mid] > left and mat[row_index][mid] > right:
                return [row_index,mid]

            elif left > mat[row_index][mid]:
                high = mid - 1

            else:
                low = mid + 1

        return -1


            
        