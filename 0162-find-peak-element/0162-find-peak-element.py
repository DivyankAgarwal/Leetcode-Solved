class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        #brute

        # for i in range(0, len(nums)):
        #     if (i == 0 or (nums[i] > nums[i-1])) and (i == len(nums)-1 or nums[i] > nums[i+1]):
        #         return i
        

        # return 0

        #better
        n = len(nums)
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[n-1] > nums[n-2]:
            return n-1

        low = 1
        high = len(nums) - 2

        while low<=high:
            mid = low + (high - low) // 2

            if mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            elif mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:
                return mid
            else:

                if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid-1] > nums[mid]:
                    high = mid - 1

                else:
                    low = mid + 1
        return -1

            