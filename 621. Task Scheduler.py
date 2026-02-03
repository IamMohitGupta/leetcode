class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        max_freq = max(freq.values())
        count_max=0
        for v in freq.values():
            if v == max_freq:
                count_max+=1

        return max(len(tasks), (max_freq - 1)*(n + 1)+count_max)

"""

Approach:

Gap size = n
Block size = n + 1
Blocks = max_freq - 1
Tail width = count_max

"""
