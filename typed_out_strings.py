"""
Given two strings S and T return if they equal when both are typed out. Any # that appears in the string counts as backspaces


1. can there be multiple # ? what happens if there are ## ??
2. what happens if there is # and there are no chars to remove ? dont do anything
3. is it case insensitive ? no 'A is not a'

"""


class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        s1 = []
        s2 = []

        def add_to_stack(array, stack):
            for char in array:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        s1 = add_to_stack(s, s1)
        s2 = add_to_stack(t, s2)
        return s1 == s2


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        s_ptr = len(s) - 1
        t_ptr = len(t) - 1

        while s_ptr >= 0  or t_ptr >=0:
            if s[s_ptr] == "#" or t[t_ptr] == '#':
                if s[s_ptr] == '#':
                    backcount = 2
                    while backcount:
                        s_ptr -= 1
                        backcount -= 1
                        if s_ptr >=0 and s[s_ptr] == '#':
                            backcount += 2
                if t[t_ptr] == '#':
                    backcount = 2
                    while backcount:
                        t_ptr -= 1
                        backcount -= 1
                        if t_ptr >= 0 and t[t_ptr] == '#':
                            backcount += 2
            else:
                if s[s_ptr] != t[t_ptr]:
                    return False
                else:
                    s_ptr -= 1
                    t_ptr -= 1
        return True


S = "ab#c"
T = "ad#c"
# print(Solution1().backspaceCompare(S,T))
# print(Solution().backspaceCompare(S, T))
# S = "badc"
# T = "adc"
# print(Solution1().backspaceCompare(S,T))
# print(Solution().backspaceCompare(S,T))
S = "ab##"
T = "c#d#"
# print(Solution().backspaceCompare(S,T))

S = "aaa###a"
T = "aaaa###a"
print(Solution().backspaceCompare(S,T))
