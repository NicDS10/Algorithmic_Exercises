class Solution:
    def climbStairs(self, n: int) -> int:
        uno = 2
        due = 1
        for i in range(3, n):
            dv = due
            due = uno
            uno = dv + due

        if n <= 3:
            return n
        else:
            return due + uno