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
