# 14. Longest Common Prefix
# Easy
# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# for i in strs:
#     for j in i:
#

# try:
#     if j == strs[strs.index(i)+1][i.index(j)] == strs[strs.index(i)+2][i.index(j)]:
#         if j not in prefix:
#             prefix += j
#     else:
#         break
# except IndexError:
#     break

def longest_common_prefix(strs: list[str]):
    prefix = ""
    strs = strs[::-1]
    letter_matches = True
    cur_i = 0
    while letter_matches and strs:
        cur_l = strs[0][cur_i] # 1. flight[0] = f
        for i in strs: # 1. flight 2. flow
            try:
                if cur_l == strs[1][cur_i]: # f == flow[0]=f
                    letter_matches = True
                else:
                    letter_matches = False
            except IndexError:
                break
        prefix += cur_l
        cur_i += 1
        print(prefix)
        strs.pop(0)

    print(prefix)


longest_common_prefix(["flower", "flow", "flight"])

