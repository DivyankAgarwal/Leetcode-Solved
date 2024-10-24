import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        #brute
        # student_score = collections.defaultdict(list)

        # for id, score in items:
        #     student_score[id].append(score)

        # result = []

        # for id in student_score.keys():

        #     scores = student_score[id]

        #     scores.sort(reverse = True)

        #     top5scores = scores[:5]

        #     avg = sum(top5scores) // 5

        #     result.append([id, avg])

        # result.sort(key = lambda x: x[0])

        # return result

        # Optimized - using heap


        student_score = collections.defaultdict(list)

        for id, score in items:
            heapq.heappush(student_score[id], score)
            if len(student_score[id]) > 5:
                heapq.heappop(student_score[id])

            
            
        print(student_score)

        result = []
        

        for id, score in sorted(student_score.items()):
           
            avg = sum(score) // len(score)
            result.append([id,avg])

        return result




        