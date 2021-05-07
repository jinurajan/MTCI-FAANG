"""
given a string find the length of the longest substring without repeating characters.

Questions
1. can the string be empty ?
2. is the substring contigous ?
3. is the characters case senstive ?
"""
from collections import Counter

def longest_substring(s):
    if not s:
        return 0
    char_map = Counter()
    left = 0
    right = 0
    max_len = 0
    while right < len(s):
        char_map[s[right]] += 1
        while char_map[s[right]] > 1:
            char_map[s[left]] -= 1
            left += 1
        max_len = max(max_len, right-left+1)
        right += 1
    return max_len


def longest_substring_1(s):
    if not s:
        return 0
    char_set = set()
    max_len = 0
    left = 0
    right = 0
    while right < len(s):
        if s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, len(char_set))
        right += 1
    return max_len

s = "abcabcbb"
print(longest_substring(s))
print(longest_substring_1(s))
s ="bbbbb"
print(longest_substring(s))
print(longest_substring_1(s))
s = "pwwkew"
print(longest_substring(s))
print(longest_substring_1(s))
s = ""
print(longest_substring(s))
print(longest_substring_1(s))

