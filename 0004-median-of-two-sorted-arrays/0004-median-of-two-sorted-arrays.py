class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        num1Length = len(nums1)
        num2Length = len(nums2)

        start = 0
        end = num1Length

        while (start <= end):
            partX = start  + (end - start) // 2 #mid
            partY = ( (num1Length + num2Length + 1) // 2) - partX

            if partX == 0:
                maxLeftX = -float('inf')
            else:
                maxLeftX = nums1[partX - 1]
            
            if partY == 0:
                maxLeftY = -float('inf')
            else:
                maxLeftY = nums2[partY - 1]
            
            if partX == num1Length:
                minRightX = float('inf')
            else:
                minRightX = nums1[partX]


            if partY == num2Length:
                minRightY = float('inf')
            else:
                minRightY = nums2[partY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (num1Length + num2Length) % 2 == 0:
                    a = max(maxLeftX, maxLeftY)
                    b = min(minRightX,minRightY)
                    return (a+b) / 2
                else:
                    return max(maxLeftX, maxLeftY)
                    
            elif maxLeftX > minRightY:
                end = partX - 1
            else:
                start = partX + 1

        if num1Length == 0:
            if num2Length % 2 == 0:
                return (nums2[num2Length // 2 - 1] + nums2[num2Length // 2]) / 2
            else:
                return nums2[num2Length // 2]

        