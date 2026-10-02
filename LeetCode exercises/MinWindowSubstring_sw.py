from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        conta = 0
        include = len(t)
        used = Counter(t)
        current = dict()
        for key in used:
            current[key] = 0

        if len(s) < len(t):
            return ""

        inizio = 0
        fine = 0
        best = ""
        while fine < len(s) or conta >= include:
            while conta < include and fine < len(s):
                if s[fine] in current:
                    if current[s[fine]] < used[s[fine]]:
                        conta += 1
                    current[s[fine]] += 1
                if fine < len(s):
                    fine += 1

            while conta == include:
                if len(best) > 0:
                    if len(s[inizio: fine]) < len(best):
                        best = s[inizio: fine]
                else:
                    best = s[inizio: fine]

                if s[inizio] in current:
                    current[s[inizio]] -= 1
                    if current[s[inizio]] < used[s[inizio]]:
                        conta -= 1
                inizio += 1

        return best