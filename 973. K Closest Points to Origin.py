class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = {}
        for i in range(len(points)):
            m[i] = points[i][0]**2 + points[i][1]**2

        m = dict(sorted(m.items(), key=lambda item: item[1]))

        l = []
        for i in m:
            if k == 0:
                break
            l.append(points[i])
            k -= 1

        return l
