class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        total_sum = 0
        mini = float('inf')
        neg_count = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                total_sum += abs(matrix[row][col])
                mini = min(mini, abs(matrix[row][col]))
                if matrix[row][col] < 0:
                    neg_count +=1

        if neg_count % 2 != 0 :
            total_sum -= 2 * mini

        return total_sum


        