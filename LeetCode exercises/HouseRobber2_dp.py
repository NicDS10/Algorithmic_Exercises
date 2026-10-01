class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def rob_houses(houses):
            tabulation = [houses[0], max(houses[0], houses[1])]
            for ind, i in enumerate(houses[2::]):
                tabulation.append(max(tabulation[ind] + i, tabulation[ind + 1]))

            return tabulation[-1]

        return max(rob_houses(nums[:len(nums) - 1]), rob_houses(nums[1:]))