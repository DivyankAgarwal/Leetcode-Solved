class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute
        # mini = float('inf')
        # for n in nums:
        #     if mini > n:
        #         mini = n
        # return mini


        ans = float('inf')

        low = 0
        high = len(nums) - 1

        while low<=high:
            mid = low + (high - low) // 2

            # if nums[low] <= nums[mid] <= nums[high]:
            #     ans = min(ans, nums[low])
            #     break

            #check if left is sorted. The idea is rotating point will always have the lowest element. 
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low]) # no at position low is always be less than mid. We got the min. 
                #Now dont check if left part. we already got mini element in left sorted part. check in right.Hence low = mid + 1

                low = mid + 1 

            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        
        return ans

        