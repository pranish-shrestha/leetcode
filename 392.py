'''
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0

        if not s:
            return True

        for i in range(len(t)):
            if t[i] == s[index]:
                index += 1
            if index == len(s):
                return True
        return False
