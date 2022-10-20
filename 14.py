'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
def longestCommonPrefix(strs) -> str:
    current_string = ""
    strs = sorted(strs)
    
    for i in range(len(min(strs[0], strs[len(strs)-1]))):
        if strs[0][i] == strs[len(strs)-1][i]:
            current_string += strs[0][i]
        else:
            return current_string
    return current_string

print(longestCommonPrefix(["dog","racecar","car"]))