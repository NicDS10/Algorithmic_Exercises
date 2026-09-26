import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def division(numeri, limite, divisore):
            somma = 0
            for num in numeri:
                somma += math.ceil(num / divisore)

            if somma <= limite:
                return True
            else:
                return False

        left = -(-sum(nums) // threshold)
        right = max(nums)
        best = right
        while left <= right:
            mid = (left + right) // 2

            if division(nums, threshold, mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1

        return best