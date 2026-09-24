class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def check(pesi, giorni_tot, opt):
            giorni_correnti = 1
            peso_attuale = 0
            for i in pesi:
                if peso_attuale + i > opt:
                    giorni_correnti += 1
                    peso_attuale = i
                else:
                    peso_attuale += i

            if giorni_correnti <= giorni_tot:
                return True
            else:
                return False

        left = max(weights)
        right = left * math.ceil(len(weights) / days)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(weights, days, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans