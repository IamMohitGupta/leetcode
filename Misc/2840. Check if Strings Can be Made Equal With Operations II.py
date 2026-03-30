class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = [0] * 26
        odd1 = [0] * 26
        even2 = [0] * 26
        odd2 = [0] * 26

        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')

            if i % 2 == 0:
                even1[idx1] += 1
                even2[idx2] += 1
            else:
                odd1[idx1] += 1
                odd2[idx2] += 1

        return even1 == even2 and odd1 == odd2
