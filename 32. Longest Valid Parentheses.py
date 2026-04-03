class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        result = []
        if len(s) == 0:
            return 0

        for i in s:
            if i == '(':
                stack.append(len(result))
                result.append('I')
            else:
                if stack:
                    idx = stack.pop()
                    result[idx] = 'V'
                    result.append('V')
                else:
                    result.append('I')
        res=0
        temp = 0
        for val in result:
            if val == "V":
                temp += 1
            else:
                res = max(res, temp)
                temp = 0
        res = max(res, temp)
        return res
