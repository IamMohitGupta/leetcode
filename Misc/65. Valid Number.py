class Solution:
    def isNumber(self, s: str) -> bool:
        sign = False
        exponent = False
        decimal = False
        digit = False

        for i in range(len(s)):
            if s[i].isdigit():
                digit = True
            elif s[i] == '.':
                if decimal or exponent:
                    return False
                decimal = True
            elif s[i] == 'e' or s[i] == 'E':
                if exponent or not digit:
                    return False
                exponent = True
                digit = False
            elif s[i] == '+' or s[i] == '-':
                if i != 0 and s[i-1] not in ['e','E']:
                    return False
            else:
                return False
        return digit
