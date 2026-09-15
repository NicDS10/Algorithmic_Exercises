class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ps = [0]
        for i in nums:
            ps.append(i + ps[-1])

        if ps[-1] < target:
            return 0

        risultato = float("inf")

        for ind, num in enumerate(nums):
            inizio = ind + 1
            fine = len(nums)
            while inizio <= fine:
                mid = (inizio + fine) // 2
                if ps[mid] - ps[ind] >= target:
                    risultato = min(risultato, mid - ind)
                    fine = mid - 1
                else:
                    inizio = mid + 1

        return risultato