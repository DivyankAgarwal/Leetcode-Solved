class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col] == target:
        #             return True

        # return False

        #binary serach -> check row by row

        def binarysearch(data, n):
            low = 0
            high = len(data)-1

            while low <= high:
                mid = low + (high - low) // 2

                if target == data[mid]:
                    return True

                elif target > data[mid]:
                    low = mid + 1

                else:
                    high = mid - 1


            return False

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][cols - 1]:
                return binarysearch(matrix[i], rows)

        return False

        