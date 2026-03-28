class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for i in arr:
            if len(set(i)) < len(i):
                continue
            x = set(i)
            for j in dp:
                if x&j:
                    continue
                dp.append(x|j)

        max_len = 0

        for a in dp:
            if len(a) > max_len:
                max_len = len(a)

        return max_len

"""

Approach:
Keep a dp that contains set with unique characters, if you and 2 words and result is not 0, that means something is duplicate.
If result 0 then append two words OR
Return max length

"""
