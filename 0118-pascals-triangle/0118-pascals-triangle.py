class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        result = []
        result.append([1])
        result.append([1,1])



        for i in range(2, numRows):
            new_row = []
            new_row.append(1)

            prev_row = result[i-1]

            for j in range(0,i-1):
                new_row.append(prev_row[j]+prev_row[j+1])

            new_row.append(1)
            result.append(new_row)
        
        return result

        