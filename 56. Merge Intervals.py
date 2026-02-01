class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        new_interval = []
        curr_start, curr_end = intervals[0]
        for i in range(1,len(intervals)):
            next_start, next_end = intervals[i]
            if curr_end >= next_start:
                curr_end = max(curr_end, next_end)
            else:
                new_interval.append([curr_start, curr_end])
                curr_start, curr_end = next_start, next_end
        new_interval.append([curr_start, curr_end])
        return new_interval

"""

Sort → Grow the current interval → Push when broken.

"""
