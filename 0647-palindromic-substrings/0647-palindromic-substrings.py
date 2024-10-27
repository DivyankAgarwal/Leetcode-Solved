class Solution:
    def countSubstrings(self, s: str) -> int:

        #brute TC O(n3)

        # def check_if_palindrome(s):
        #     return s == s[::-1]

        # count = 0
        # n = len(s)

        # for i in range(n):
        #     for j in range(i,n):
        #         if check_if_palindrome(s[i:j+1]):
        #             count+=1


        # return count


        #optimized


        def check_around_center(left, right):

            nonlocal count, palindromic_substrings

            while left >=0 and right < n and s[left] == s[right]:
                palindromic_substrings.append(s[left:right+1])
                count+=1
                left -=1
                right +=1


        n = len(s)
        count = 0
        palindromic_substrings = []

        for i in range(n):

            check_around_center(i,i)


            check_around_center(i,i+1)

        # print(palindromic_substrings)

        return count


        