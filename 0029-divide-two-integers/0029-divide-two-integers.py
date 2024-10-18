class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # brute
        # if dividend == divisor:
        #     return 1

        # if dividend == 0:
        #     return 0

        # negative = (dividend < 0) != (divisor < 0)

        # # Convert both numbers to positive
        # dividend, divisor = abs(dividend), abs(divisor)

        # quotient = 0

        # while dividend >= divisor:
        #     dividend -= divisor
        #     quotient += 1

        # return -quotient if negative else quotient

        # optimal

        if divisor == dividend:
            return 1

        if dividend == 0:
            return 0

        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        negative = (dividend < 0) != (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dividend -= temp_divisor
            quotient += multiple

        return -quotient if negative else quotient
