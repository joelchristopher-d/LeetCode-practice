class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # res = dividend/divisor
        return int(dividend/divisor) if dividend/divisor<(2**31) else int(dividend/divisor)-1
