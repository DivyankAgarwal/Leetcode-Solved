class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # if k == 0:
        #     return

        # n = len(nums)

        # if k > n:
        #     k = k % n

        # temp = []

        
        # for i in range(n - k, n):
        #     temp.append(nums[i])

      
        # for i in range(n - k - 1, -1, -1):
        #     nums[i + k] = nums[i]

       
        # for i in range(k):
        #     nums[i] = temp[i]


        #better

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -=1

        
        n = len(nums)

        if k > n:
            k = k % n

        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        
        