class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        #brute
        student_score = collections.defaultdict(list)

        for id, score in items:
            student_score[id].append(score)

        result = []

        for id in student_score.keys():

            scores = student_score[id]

            scores.sort(reverse = True)

            top5scores = scores[:5]

            avg = sum(top5scores) // 5

            result.append([id, avg])

        result.sort(key = lambda x: x[0])

        return result

        

        return result.sort(key= lambda x: x[0])

        