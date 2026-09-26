class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        num_bananas = sum(piles)
        n = len(piles)

        def mangia_banane(ore, media, bananas):
            conta = 0
            for i in bananas:
                conta += -(-i // media)

            if conta <= ore:
                return True
            else:
                return False

        best = 0

        left = -(-num_bananas // h)
        right = -(-(num_bananas - n + 1) // (h - n + 1))
        while left <= right:
            k = (left + right) // 2
            if mangia_banane(h, k, piles):
                right = k - 1
                best = k
            else:
                left = k + 1

        return best