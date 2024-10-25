class Solution:
    def maxArea(self, height: List[int]) -> int:

        #brute
        # max_area = 0
        # n = len(height)

        # for i in range(n):
        #     for j in range(i+1, n):

        #         area = (j-i) * min(height[j], height[i])
        #         max_area = max(max_area, area)

        # return max_area
        
        #Optimized

        left = 0
        right = len(height) - 1
        max_area = 0

        while left <= right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                
                left +=1

            else:
                area = (right - left) * height[right]
                right -=1

            max_area = max(max_area, area)
        
        return max_area