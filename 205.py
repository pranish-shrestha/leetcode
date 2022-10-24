'''
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1
'''


def isIsomorphic(s: str, t: str) -> bool:

    hash_ = dict()
    for i in range(len(s)):
        if s[i] not in hash_ and t[i] not in hash_.values():
            hash_[s[i]] = t[i]
        elif s[i] in hash_:
            if hash_[s[i]] != t[i]:
                return False
        else:
            return False
    return True


