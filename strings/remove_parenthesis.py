"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened_count = 0
        result = []

        for i in s:
            if i == '(':
                if opened_count>0:
                    result.append(i)
                opened_count += 1
            elif i == ')':
                opened_count -= 1
                if opened_count>0:
                    result.append(i)
        return "".join(result)