class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result = []
        count1 = 0

        for index, data in enumerate(mat):
            count1 = 0
            for entry in data:
                if entry == 1:
                    count1 +=1
            
            if count1 != 0:
                result.append([index,count1])

        if all(count == 0 for _, count in result):
            return [0, 0]


        result.sort(key=lambda x: (-x[1], x[0]))
        return result[0]