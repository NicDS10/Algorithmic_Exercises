class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ps = [0]
        for i in nums:
            ps.append(i + ps[-1])

        if len(nums) < 2:
            if nums[0] >= target:
                return 1
            else:
                return 0
        else:
            if ps[-1] < target:
                return 0

            for ind, s in enumerate(ps):
                if ps[-1] - s < target:
                    return len(ps) - ind
                if ind == len(nums):
                    return 1