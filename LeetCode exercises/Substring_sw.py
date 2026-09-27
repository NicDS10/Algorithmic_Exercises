class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ultimo_visto = {}
        inizio = 0
        massimo = 0

        for fine, char in enumerate(s):
            if char in ultimo_visto and ultimo_visto[char] >= inizio:
                inizio = ultimo_visto[char] + 1

            ultimo_visto[char] = fine
            massimo = max(massimo, fine - inizio + 1)

        return massimo