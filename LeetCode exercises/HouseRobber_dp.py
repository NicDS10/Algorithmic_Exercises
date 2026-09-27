class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        tabulation = [nums[0], max(nums[0], nums[1])]
        for ind, i in enumerate(nums[2::]):
            tabulation.append(max(tabulation[ind] + i, tabulation[ind + 1]))

        return tabulation[-1]