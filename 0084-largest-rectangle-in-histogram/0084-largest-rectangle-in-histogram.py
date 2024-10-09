class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #brute
        # area = 0

        # for i in range(len(heights)):
        #     min_h = float('inf')

        #     for j in range(i, len(heights)):

        #         min_h = min(min_h, heights[j])
        #         width = j-i+1
        #         area = max(area, min_h*width)


        # return area        
        
        #optimal

        if len(heights) == 1:
            return heights[0]

        def get_nse(arr):
            stack = []
            result = [len(arr)]*len(arr)
            for i in range(len(arr)):
                while stack and arr[stack[-1]] > arr[i]:
                    curr = stack.pop() 
                    result[curr] = i 
                stack.append(i)
            return result

        def get_pse(arr):
            stack = []
            result = [-1]*len(arr)
            for i in range(len(arr)):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop() 
                if len(stack) > 0:
                    result[i] = stack[-1]
                stack.append(i)
            return result


        nse = get_nse(heights)
        pse = get_pse(heights)

        largestArea = 0
        
        
        area = 0
        
       
        for i in range(len(heights)):
            
            # Calculate current area
            area = heights[i] * (nse[i]-pse[i]-1)
            
            # Update largest area
            largestArea = max(largestArea, area)
        
        # Return largest area found
        return largestArea
        